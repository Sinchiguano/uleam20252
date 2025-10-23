export default function Table({ columns = [], rows = [], actions }) {
  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          {columns.map((c) => (
            <th key={c.key} style={{ textAlign: "left", borderBottom: "1px solid #ddd", padding: 8 }}>
              {c.title}
            </th>
          ))}
          {actions && <th style={{ width: 160 }}></th>}
        </tr>
      </thead>
      <tbody>
        {rows.map((r) => (
          <tr key={r.id}>
            {columns.map((c) => (
              <td key={c.key} style={{ borderBottom: "1px solid #f0f0f0", padding: 8 }}>
                {r[c.key]}
              </td>
            ))}
            {actions && <td style={{ padding: 8 }}>{actions(r)}</td>}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
