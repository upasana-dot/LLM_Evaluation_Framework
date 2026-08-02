import { useState } from "react";

export default function PromptForm({ onEvaluate, loading }) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = () => {
    if (!prompt.trim()) return;
    onEvaluate(prompt);
  };

  return (
    <div className="bg-slate-800 rounded-xl p-6 shadow-lg">
      <textarea
        rows={6}
        className="w-full rounded-lg p-4 bg-slate-900 text-white border border-slate-700"
        placeholder="Enter your prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="mt-5 px-6 py-3 rounded-lg bg-cyan-500 hover:bg-cyan-600 text-white font-semibold"
      >
        {loading ? "Evaluating..." : "Evaluate Prompt"}
      </button>
    </div>
  );
}