import axios from "axios";

const API_URL = "https://auth-backend.onrender.com";

export const registerUser = (data) => axios.post(`${API_URL}/auth/register`, data);
export const loginUser = (data) => axios.post(`${API_URL}/auth/login`, data);
export const submitForm = (data) => axios.post(`${API_URL}/submit`, data);
