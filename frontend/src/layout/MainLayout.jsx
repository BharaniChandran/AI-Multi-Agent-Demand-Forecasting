import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Footer from "../components/Footer";

function MainLayout({ children }) {
  return (
    <div className="d-flex flex-column min-vh-100">

      <Navbar />

      <div className="d-flex flex-grow-1">

        <Sidebar />

        <main className="flex-grow-1 p-4">
          {children}
        </main>

      </div>

      <Footer />

    </div>
  );
}

export default MainLayout;