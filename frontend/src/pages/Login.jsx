import { useState } from "react";
import axios from "axios";
import { API_BACKEND } from "../constants";
import { useNavigate } from "react-router";
import {setIsLoggedIn} from '../utils'

export default function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");

    const navigate = useNavigate()

    const handleLogin = async () => {
        try {
            const response = await axios.get(API_BACKEND + "/user/" + username, {
                username,
            });
            if (password === response.data.password) {
                setIsLoggedIn(true)
                navigate("/")
                return
            }

            setMessage(response.data.message);
        } catch (error) {
            setMessage(error.response?.data?.detail || "Login failed");
        }
    };

    return (
        <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh" }}>
            <div style={{ width: "300px", padding: "20px", boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", borderRadius: "8px", backgroundColor: "white" }}>
                <h2 style={{ textAlign: "center", marginBottom: "20px" }}>Login</h2>
                <input
                    style={{ width: "100%", padding: "10px", marginBottom: "10px", border: "1px solid #ccc", borderRadius: "4px" }}
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    style={{ width: "100%", padding: "10px", marginBottom: "10px", border: "1px solid #ccc", borderRadius: "4px" }}
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button
                    style={{ width: "100%", padding: "10px", backgroundColor: "blue", color: "white", border: "none", borderRadius: "4px", cursor: "pointer" }}
                    onClick={handleLogin}
                >
                    Login
                </button>
                {message && <p style={{ textAlign: "center", color: "red", marginTop: "10px" }}>{message}</p>}
            </div>
        </div>
    );
}
