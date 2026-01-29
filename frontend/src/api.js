import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000",
});

export const registerUser = (data) => API.post("/auth/register", data);

export const loginUser = (data) => API.post("/auth/login", data);

export const submitForm = (data) =>
  API.post("/form/submit-form", data);
