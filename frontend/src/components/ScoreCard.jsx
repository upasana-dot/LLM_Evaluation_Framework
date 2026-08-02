export default function ScoreCard({ score }) {
    return (
      <div className="bg-cyan-600 rounded-xl p-6 text-center text-white shadow-xl">
        <h2 className="text-xl">Overall Score</h2>
  
        <h1 className="text-6xl font-bold mt-4">
          {score}
        </h1>
      </div>
    );
  }