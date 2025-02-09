// Signup.js
import React, { useState } from "react";
import axios from "axios";
import { API_BACKEND } from "../constants";
import { useNavigate } from "react-router";

export const Signup = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    const userData = {
      username,
      password,
    };

    try {
      const response = await axios.post(API_BACKEND + "/signup" + "?username=" + username + "&password=" + password);
      console.log("Signup successful", response.data);
      navigate("/login")
    } catch (err) {
      setError("Signup failed. Please try again.");
      console.error("Error during signup", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <div>
          <button type="submit" disabled={loading}>
            {loading ? "Submitting..." : "Sign Up"}
          </button>
        </div>
      </form>
    </div>
  );
};

