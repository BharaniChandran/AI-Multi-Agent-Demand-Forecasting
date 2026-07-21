const forecastData = [
  {
    id: 1,
    product: "Laptop",
    predictedDemand: 120,
    confidence: "95%",
  },
  {
    id: 2,
    product: "Smartphone",
    predictedDemand: 250,
    confidence: "93%",
  },
  {
    id: 3,
    product: "Headphones",
    predictedDemand: 180,
    confidence: "91%",
  },
];

export default function ProductTable() {
  return (
    <div className="card shadow-sm mt-4">
      <div className="card-body">
        <h4 className="mb-3">Forecast Results</h4>

        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>Product</th>
              <th>Predicted Demand</th>
              <th>Confidence</th>
            </tr>
          </thead>

          <tbody>
            {forecastData.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.product}</td>
                <td>{item.predictedDemand}</td>
                <td>{item.confidence}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}