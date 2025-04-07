import React, { useState } from "react";
import axios from "axios";

function TracerouteForm({ setRoute }) {
  const [domain, setDomain] = useState("");

  const handleQuery = async () => {
    if (!domain) return alert("Please enter a domain");

    try {
      const response = await axios.post("http://127.0.0.1:5000/traceroute", { domain })
      console.log("✅ API Response:", response.data);
      setRoute(response.data.route);
    } catch (error) {
      console.error("❌ Fetch Error:", error);
      alert("Failed to fetch traceroute data.");
    }
  };

  return (
    <div>
      <input 
        type="text" 
        value={domain} 
        onChange={(e) => setDomain(e.target.value)} 
        placeholder="Enter domain name"
      />
      <button onClick={handleQuery}>Query</button>
    </div>
  );
}

export default TracerouteForm;

