export default function MetricCard({ title, value, color }) {
    return (
      <div className="bg-slate-800 rounded-xl p-5 shadow-lg">
        <h3 className="text-gray-400">{title}</h3>
  
        <p className={`text-3xl font-bold mt-3 ${color}`}>
          {value}
        </p>
      </div>
    );
  }