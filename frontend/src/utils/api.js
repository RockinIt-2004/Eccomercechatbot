import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000", // ✅ Flask backend server
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token"); // or use Context
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
