import { useNavigate } from "react-router-dom";

export default function Logout() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("user_id"); // Clear user ID
    alert("Logged out successfully!");
    navigate("/login");
  };

  return <button onClick={handleLogout}>Logout</button>;
}
