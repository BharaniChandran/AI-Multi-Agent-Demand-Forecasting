import ForecastCard from "../components/ForecastCard";

export default function Dashboard() {
  return (
    <div className="container-fluid">

      <h2 className="mb-4">
        AI Multi-Agent Product Demand Forecasting Dashboard
      </h2>

      <div className="row">

        <ForecastCard
          title="Total Products"
          value="250"
          color="primary"
        />

        <ForecastCard
          title="Forecasts Generated"
          value="125"
          color="success"
        />

        <ForecastCard
          title="Model Accuracy"
          value="94.8%"
          color="warning"
        />

      </div>

      <div className="card shadow-sm mt-4">
        <div className="card-body">
          <h4>Project Status</h4>

          <table className="table table-striped mt-3">
            <thead>
              <tr>
                <th>Module</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>
              <tr>
                <td>Frontend</td>
                <td>✅ Completed</td>
              </tr>

              <tr>
                <td>Backend</td>
                <td>🚧 In Progress</td>
              </tr>

              <tr>
                <td>ML Model</td>
                <td>🚧 In Progress</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
}