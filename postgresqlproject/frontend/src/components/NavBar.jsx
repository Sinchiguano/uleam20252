import { Link, useLocation } from "react-router-dom";

export default function NavBar() {
  const { pathname } = useLocation();
  const linkStyle = (to) => ({
    padding: "8px 12px",
    marginRight: 8,
    textDecoration: "none",
    color: pathname === to ? "#fff" : "#333",
    background: pathname === to ? "#2563eb" : "#e5e7eb",
    borderRadius: 8
  });

  return (
    <nav style={{ padding: 12, borderBottom: "1px solid #e5e7eb" }}>
      <Link to="/students" style={linkStyle("/students")}>Students</Link>
      <Link to="/courses" style={linkStyle("/courses")}>Courses</Link>
      <Link to="/enrollments" style={linkStyle("/enrollments")}>Enrollments</Link>
    </nav>
  );
}
