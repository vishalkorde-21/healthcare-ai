import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    name: "",
    age: "",
    symptoms: "",
  });

  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/create/",
        form
      );
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="container">
      <h2>Healthcare AI</h2>

      <input
        type="text"
        placeholder="Name"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
      />

      <input
        type="number"
        placeholder="Age"
        value={form.age}
        onChange={(e) => setForm({ ...form, age: e.target.value })}
      />

      <input
        type="text"
        placeholder="Symptoms"
        value={form.symptoms}
        onChange={(e) =>
          setForm({ ...form, symptoms: e.target.value })
        }
      />

      <button onClick={handleSubmit}>Predict</button>

      {result && (
        <div className="result">
          <p><b>Disease:</b> {result.diagnosis}</p>
          <p><b>Treatment:</b> {result.treatment}</p>
        </div>
      )}
    </div>
  );
}

export default App;