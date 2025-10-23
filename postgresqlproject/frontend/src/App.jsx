import { Routes, Route, Navigate, Link } from "react-router-dom";
import Students from "./pages/Students.jsx";
import Courses from "./pages/Courses.jsx";
import Enrollments from "./pages/Enrollments.jsx";
import NavBar from "./components/NavBar.jsx";

export default function App() {
  return (
    <div style={{ fontFamily: "system-ui, sans-serif" }}>
      <NavBar />
      <div style={{ maxWidth: 960, margin: "20px auto", padding: 16 }}>
        <Routes>
          <Route path="/" element={<Navigate to="/students" replace />} />
          <Route path="/students" element={<Students />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/enrollments" element={<Enrollments />} />
          <Route path="*" element={<div>Not Found. <Link to="/">Go Home</Link></div>} />
        </Routes>
      </div>
    </div>
  );
}
