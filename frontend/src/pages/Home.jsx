import { useState } from "react";
import Navbar from "../components/Navbar";
import PromptForm from "../components/PromptForm";
import ScoreCard from "../components/ScoreCard";
import MetricCard from "../components/MetricCard";
import API from "../services/api";

export default function Home() {

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const evaluatePrompt = async (prompt) => {
    try {
      setLoading(true);

      const response = await API.post("/evaluate", {
        prompt: prompt,
      });

      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Backend Error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-900">
      <Navbar />

      <div className="max-w-6xl mx-auto p-8">

        <PromptForm
          onEvaluate={evaluatePrompt}
          loading={loading}
        />

        <div className="mt-8">
          <ScoreCard
            score={result ? result.overall.overall_score : "--"}
          />
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-5 mt-8">

          <MetricCard
            title="Bias"
            value={result ? result.bias.risk_level : "--"}
            color="text-green-400"
          />

          <MetricCard
            title="Toxicity"
            value={result ? result.toxicity.risk_level : "--"}
            color="text-red-400"
          />

          <MetricCard
            title="Safety"
            value={result ? result.safety.risk_level : "--"}
            color="text-blue-400"
          />

          <MetricCard
            title="Factual"
            value={result ? result.factual_accuracy.confidence : "--"}
            color="text-yellow-400"
          />

          <MetricCard
            title="Hallucination"
            value={result ? result.hallucination.risk_level : "--"}
            color="text-purple-400"
          />

        </div>

        {result && (
          <div className="mt-8 bg-slate-800 rounded-xl p-6">
            <h2 className="text-2xl font-bold text-cyan-400 mb-4">
              LLM Response
            </h2>

            <p className="text-gray-300 whitespace-pre-wrap">
              {result.response}
            </p>
          </div>
        )}

      </div>
    </div>
  );
}