import React, { useState } from "react";
import axios from "axios";

function App() {
  const [form, setForm] = useState({
    name: "",
    age: "",
    symptoms: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

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
    <div style={{ padding: "20px" }}>
      <h2>Healthcare AI</h2>

      <input name="name" placeholder="Name" onChange={handleChange} /><br /><br />
      <input name="age" placeholder="Age" onChange={handleChange} /><br /><br />
      <input name="symptoms" placeholder="Symptoms" onChange={handleChange} /><br /><br />

      <button onClick={handleSubmit}>Predict</button>

      {result && (
        <div>
          <h3>Result:</h3>
          <p><b>Disease:</b> {result.diagnosis}</p>
          <p><b>Treatment:</b> {result.treatment}</p>
        </div>
      )}
    </div>
  );
}

export default App;