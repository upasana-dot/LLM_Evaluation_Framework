export default function Navbar() {
    return (
      <nav className="bg-slate-800 shadow-lg border-b border-slate-700">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-cyan-400">
            LLM Evaluation Framework
          </h1>
  
          <p className="text-gray-300">
            Bias • Toxicity • Safety • Accuracy
          </p>
        </div>
      </nav>
    );
  }