export default function Dashboard() {
  return (
    <div className="container mt-5">
      <h1 className="text-primary">
        AI Multi-Agent Product Demand Forecasting System
      </h1>

      <hr />

      <h3>Dashboard</h3>

      <p>
        Welcome to the Product Demand Forecasting Dashboard.
      </p>

      <div className="row mt-4">

        <div className="col-md-4">
          <div className="card shadow p-3">
            <h4>Total Products</h4>
            <h2>0</h2>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card shadow p-3">
            <h4>Forecasts</h4>
            <h2>0</h2>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card shadow p-3">
            <h4>Accuracy</h4>
            <h2>0%</h2>
          </div>
        </div>

      </div>
    </div>
  );
}