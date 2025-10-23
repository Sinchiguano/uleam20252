import { useEffect, useState } from "react";
import { api } from "../api";
import Table from "../components/Table";

export default function Students() {
  const [rows, setRows] = useState([]);
  const [form, setForm] = useState({ first_name: "", last_name: "", email: "", age: 18 });
  const [search, setSearch] = useState("");

  const load = async () => {
    const { data } = await api.get("/students", { params: { search } });
    setRows(data.items);
  };

  useEffect(() => { load(); }, [search]);

  const submit = async (e) => {
    e.preventDefault();
    await api.post("/students", form);
    setForm({ first_name: "", last_name: "", email: "", age: 18 });
    load();
  };

  const remove = async (id) => {
    await api.delete(`/students/${id}`);
    load();
  };

  const columns = [
    { key: "first_name", title: "First Name" },
    { key: "last_name", title: "Last Name" },
    { key: "email", title: "Email" },
    { key: "age", title: "Age" },
  ];

  return (
    <div>
      <h2>Students</h2>

      <form onSubmit={submit} style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 8, margin: "12px 0" }}>
        <input placeholder="First name" value={form.first_name} onChange={e=>setForm({...form, first_name:e.target.value})}/>
        <input placeholder="Last name"  value={form.last_name}  onChange={e=>setForm({...form, last_name:e.target.value})}/>
        <input placeholder="Email"      value={form.email}      onChange={e=>setForm({...form, email:e.target.value})}/>
        <input placeholder="Age" type="number" value={form.age} onChange={e=>setForm({...form, age:Number(e.target.value)})}/>
        <button type="submit">Add</button>
      </form>

      <input placeholder="Search name/email..." value={search} onChange={e=>setSearch(e.target.value)} style={{ marginBottom: 12, padding: 8, width: "100%" }}/>

      <Table
        columns={columns}
        rows={rows}
        actions={(r)=> <button onClick={()=>remove(r.id)}>Delete</button>}
      />
    </div>
  );
}
