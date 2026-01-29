import { useState, useEffect } from "react";
import { submitForm } from "../api";
import { useNavigate } from "react-router-dom";
import "../styles/form.css"; // 👈 import CSS

export default function Form() {
  const [field1, setField1] = useState("");
  const [field2, setField2] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const user_id = localStorage.getItem("user_id");
    if (!user_id) {
      alert("You must login first!");
      navigate("/login");
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const user_id = localStorage.getItem("user_id");
    if (!user_id) return;

    try {
      await submitForm({ user_id, field1, field2 });
      alert("Form submitted successfully!");
      setField1("");
      setField2("");
    } catch (err) {
      alert("Error submitting form");
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("user_id");
    navigate("/login");
  };

  return (
    <div className="form-container">
      <div className="form-card">
        <h2>Submit Form</h2>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Field 1"
            value={field1}
            onChange={(e) => setField1(e.target.value)}
            required
          />

          <input
            type="text"
            placeholder="Field 2"
            value={field2}
            onChange={(e) => setField2(e.target.value)}
            required
          />

          <button type="submit">Submit</button>
        </form>

        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
}
