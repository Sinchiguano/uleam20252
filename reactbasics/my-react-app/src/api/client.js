// src/api/client.js
const BASE = import.meta.env.VITE_API_URL ?? "http://localhost:5000";

export async function getServerTime() {
  const res = await fetch(`${BASE}/api/time`);
  if (!res.ok) throw new Error("API error");
  return res.json();
}
