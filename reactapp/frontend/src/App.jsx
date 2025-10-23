import { useEffect, useState } from 'react'
import axios from 'axios'

export default function App() {
  const [form, setForm] = useState({ name: '', age: '', course: '' })
  const [rows, setRows] = useState([])
  const [msg, setMsg] = useState(null)

  const load = async () => {
    const data = await axios.get('/api/students').then(r => r.data)
    setRows(data)
  }

  useEffect(() => { load() }, [])

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await axios.post('/api/students', {
        name: form.name,
        age: form.age,
        course: form.course
      })
      setMsg('Saved ✅')
      setForm({ name: '', age: '', course: '' })
      load()
    } catch (err) {
      setMsg(err?.response?.data?.error || 'Error saving')
    }
  }

  const handleDelete = async (id) => {
    await axios.delete(`/api/students/${id}`)
    load()
  }

  return (
    <div style={{ maxWidth: 720, margin: '48px auto', fontFamily: 'system-ui, Arial' }}>
      <h1>React + Flask — Student Form</h1>

      {msg && (
        <div style={{ background:'#eef', border:'1px solid #ccd', padding:8, marginBottom:12 }}
             onClick={() => setMsg(null)}>
          {msg}
        </div>
      )}

      <form onSubmit={handleSubmit}
            style={{ display:'grid', gap:12, gridTemplateColumns:'1fr 1fr', marginBottom:24 }}>
        <div style={{ gridColumn:'1 / span 2' }}>
          <label>Name<br/>
            <input name="name" value={form.name} onChange={handleChange} required
                   style={{ width:'100%', padding:8 }}/>
          </label>
        </div>
        <div>
          <label>Age<br/>
            <input name="age" type="number" min="0" max="120"
                   value={form.age} onChange={handleChange} required
                   style={{ width:'100%', padding:8 }}/>
          </label>
        </div>
        <div>
          <label>Course<br/>
            <input name="course" value={form.course} onChange={handleChange} required
                   style={{ width:'100%', padding:8 }}/>
          </label>
        </div>
        <div style={{ gridColumn:'1 / span 2', textAlign:'right' }}>
          <button type="submit" style={{ padding:'8px 16px' }}>Save</button>
        </div>
      </form>

      <table style={{ width:'100%', borderCollapse:'collapse' }}>
        <thead>
          <tr>
            <th style={th}>Name</th>
            <th style={th}>Age</th>
            <th style={th}>Course</th>
            <th style={th}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {rows.length === 0 ? (
            <tr><td colSpan="4" style={td}>No entries yet.</td></tr>
          ) : rows.map(r => (
            <tr key={r.id}>
              <td style={td}>{r.name}</td>
              <td style={td}>{r.age}</td>
              <td style={td}>{r.course}</td>
              <td style={td}>
                <button onClick={() => handleDelete(r.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

const th = { textAlign:'left', borderBottom:'1px solid #ddd', padding:'8px' }
const td = { borderBottom:'1px solid #eee', padding:'8px' }
