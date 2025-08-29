import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend
});

// attach token automatically if exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
