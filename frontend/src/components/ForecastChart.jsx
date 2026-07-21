import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function ForecastChart() {
  const data = {
    labels: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
    ],
    datasets: [
      {
        label: "Predicted Demand",
        data: [120, 180, 150, 220, 260, 300],
        borderColor: "rgb(54, 162, 235)",
        backgroundColor: "rgba(54,162,235,0.3)",
        tension: 0.4,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
    },
  };

  return (
    <div className="card shadow-sm mt-4">
      <div className="card-body">
        <h4 className="mb-3">Demand Trend Forecast</h4>

        <Line data={data} options={options} />
      </div>
    </div>
  );
}