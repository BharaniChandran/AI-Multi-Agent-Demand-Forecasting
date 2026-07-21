import { NavLink } from "react-router-dom";
import {
  FaHome,
  FaUpload,
  FaChartBar,
  FaHistory,
  FaInfoCircle,
} from "react-icons/fa";

const menuItems = [
  { path: "/", label: "Dashboard", icon: <FaHome /> },
  { path: "/upload", label: "Upload Data", icon: <FaUpload /> },
  { path: "/forecast", label: "Forecast", icon: <FaChartBar /> },
  { path: "/history", label: "History", icon: <FaHistory /> },
  { path: "/about", label: "About", icon: <FaInfoCircle /> },
];

export default function Sidebar() {
  return (
    <div
      className="bg-dark text-white p-3"
      style={{ width: "240px", minHeight: "100vh" }}
    >
      <h5 className="mb-4">Navigation</h5>

      <div className="nav flex-column">
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            end={item.path === "/"}
            className={({ isActive }) =>
              `nav-link mb-2 rounded d-flex align-items-center ${
                isActive ? "bg-primary text-white" : "text-light"
              }`
            }
          >
            <span className="me-2">{item.icon}</span>
            {item.label}
          </NavLink>
        ))}
      </div>
    </div>
  );
}