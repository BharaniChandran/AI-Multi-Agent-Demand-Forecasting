import ForecastChart from "../components/ForecastChart";
import ProductTable from "../components/ProductTable";

export default function Forecast() {
  return (
    <div className="container-fluid">

      <h2 className="mb-4">Forecast Results</h2>

      <div className="alert alert-success">
        Forecast generated successfully.
      </div>

      <ForecastChart />

      <ProductTable />

    </div>
  );
}