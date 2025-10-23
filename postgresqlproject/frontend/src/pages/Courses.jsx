import { useEffect, useState } from "react";
import { api } from "../api";
import Table from "../components/Table";

export default function Courses() {
  const [rows, setRows] = useState([]);
  const [form, setForm] = useState({ code: "", title: "", credits: 3 });
  const [search, setSearch] = useState("");

  const load = async () => {
    const { data } = await api.get("/courses", { params: { search } });
    setRows(data.items);
  };

  useEffect(() => { load(); }, [search]);

  const submit = async (e) => {
    e.preventDefault();
    await api.post("/courses", form);
    setForm({ code: "", title: "", credits: 3 });
    load();
  };

  const remove = async (id) => {
    await api.delete(`/courses/${id}`);
    load();
  };

  const columns = [
    { key: "code", title: "Code" },
    { key: "title", title: "Title" },
    { key: "credits", title: "Credits" },
  ];

  return (
    <div>
      <h2>Courses</h2>

      <form onSubmit={submit} style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 8, margin: "12px 0" }}>
        <input placeholder="Code (e.g. CS101)" value={form.code} onChange={e=>setForm({...form, code:e.target.value})}/>
        <input placeholder="Title" value={form.title} onChange={e=>setForm({...form, title:e.target.value})}/>
        <input placeholder="Credits" type="number" value={form.credits} onChange={e=>setForm({...form, credits:Number(e.target.value)})}/>
        <button type="submit">Add</button>
      </form>

      <input placeholder="Search code/title..." value={search} onChange={e=>setSearch(e.target.value)} style={{ marginBottom: 12, padding: 8, width: "100%" }}/>

      <Table
        columns={columns}
        rows={rows}
        actions={(r)=> <button onClick={()=>remove(r.id)}>Delete</button>}
      />
    </div>
  );
}
