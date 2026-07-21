const historyData = [
  {
    id: 1,
    date: "2026-07-20",
    product: "Laptop",
    demand: 120,
    accuracy: "95%",
  },
  {
    id: 2,
    date: "2026-07-19",
    product: "Smartphone",
    demand: 250,
    accuracy: "93%",
  },
  {
    id: 3,
    date: "2026-07-18",
    product: "Headphones",
    demand: 180,
    accuracy: "91%",
  },
];

export default function History() {
  return (
    <div className="container-fluid">
      <h2 className="mb-4">Forecast History</h2>

      <div className="card shadow-sm">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Product</th>
                <th>Predicted Demand</th>
                <th>Accuracy</th>
              </tr>
            </thead>

            <tbody>
              {historyData.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.date}</td>
                  <td>{item.product}</td>
                  <td>{item.demand}</td>
                  <td>{item.accuracy}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}