import { FaChartLine } from "react-icons/fa";

export default function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-primary shadow-sm px-4">
      <span className="navbar-brand mb-0 h1 d-flex align-items-center">
        <FaChartLine className="me-2" />
        AI Multi-Agent Product Demand Forecasting
      </span>
    </nav>
  );
}
