import { useEffect, useState } from "react";
import { api } from "../api";

export default function Enrollments() {
  const [students, setStudents] = useState([]);
  const [courses, setCourses] = useState([]);
  const [selStudent, setSelStudent] = useState("");
  const [selCourse, setSelCourse] = useState("");
  const [studentCourses, setStudentCourses] = useState([]);

  const load = async () => {
    const s = await api.get("/students"); setStudents(s.data.items);
    const c = await api.get("/courses"); setCourses(c.data.items);
  };

  const loadStudentCourses = async (sid) => {
    if (!sid) return setStudentCourses([]);
    const { data } = await api.get(`/students/${sid}/courses`);
    setStudentCourses(data.courses);
  };

  useEffect(()=>{ load(); }, []);
  useEffect(()=>{ loadStudentCourses(selStudent); }, [selStudent]);

  const enroll = async (e) => {
    e.preventDefault();
    if (!selStudent || !selCourse) return;
    await api.post("/enrollments", { student_id: Number(selStudent), course_id: Number(selCourse) });
    loadStudentCourses(selStudent);
  };

  const unenroll = async (cid) => {
    await api.delete("/enrollments", { data: { student_id: Number(selStudent), course_id: Number(cid) } });
    loadStudentCourses(selStudent);
  };

  return (
    <div>
      <h2>Enrollments</h2>

      <form onSubmit={enroll} style={{ display: "grid", gridTemplateColumns: "1fr 1fr 120px", gap: 8, margin: "12px 0" }}>
        <select value={selStudent} onChange={e=>setSelStudent(e.target.value)}>
          <option value="">Select student…</option>
          {students.map(s => <option key={s.id} value={s.id}>{s.first_name} {s.last_name} — {s.email}</option>)}
        </select>
        <select value={selCourse} onChange={e=>setSelCourse(e.target.value)}>
          <option value="">Select course…</option>
          {courses.map(c => <option key={c.id} value={c.id}>{c.code} — {c.title}</option>)}
        </select>
        <button type="submit">Enroll</button>
      </form>

      <div>
        <h3>Student’s Courses</h3>
        {!selStudent && <p>Select a student to view enrollments.</p>}
        {selStudent && (
          <ul>
            {studentCourses.map(c => (
              <li key={c.id} style={{ display: "flex", justifyContent: "space-between", padding: "6px 0", borderBottom: "1px solid #eee" }}>
                <span>{c.code} — {c.title} ({c.credits} cr)</span>
                <button onClick={()=>unenroll(c.id)}>Unenroll</button>
              </li>
            ))}
            {studentCourses.length === 0 && <li>No courses yet.</li>}
          </ul>
        )}
      </div>
    </div>
  );
}
