// src/App.jsx
import { useEffect, useState } from "react";

export default function App() {
  const [count, setCount] = useState(0);
  const [serverTime, setServerTime] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/api/time")
      .then(r => r.json())
      .then(data => setServerTime(data.time))
      .catch(() => setServerTime("API not available"));
  }, []);

  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <h1>React + Flask Starter</h1>
      <p>Server time: {serverTime ?? "loading..."}</p>
      <button onClick={() => setCount(c => c + 1)}>Clicks: {count}</button>
    </main>
  );
}


// import { useEffect, useState } from "react";

// export default function StudentsPage() {
//   const [rows, setRows] = useState([]);
//   useEffect(() => {
//     fetch("http://localhost:5000/api/students")
//       .then(r => r.json())
//       .then(d => setRows(d.items));
//   }, []);
//   return <ul>{rows.map(s => <li key={s.id}>{s.name}</li>)}</ul>;
// }

