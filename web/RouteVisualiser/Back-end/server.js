require("dotenv").config();
const express = require("express");
const cors = require("cors");
const traceroute = require("traceroute");
const axios = require("axios");
const { exec } = require("child_process");

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(express.json());
app.use(cors({ origin: "*", methods: "GET,POST" }));

// 📍 Route: Perform Traceroute & Get Geolocation
app.post("/traceroute", async (req, res) => {
  const { domain } = req.body;
  if (!domain) return res.status(400).json({ error: "Domain is required" });

  console.log(`🛠️ Running traceroute for: ${domain}`);

  exec(`traceroute -4 ${domain}`, async (err, stdout, stderr) => {
    if (err) {
      console.error("❌ Traceroute Error:", err);
      return res.status(500).json({ error: "Traceroute failed", details: stderr });
    }

    // Extract IPv4 addresses
    const ipRegex = /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/g;
    const ipAddresses = [...stdout.matchAll(ipRegex)].map(match => match[0]);

    console.log("✅ Extracted IPs:", ipAddresses);

    if (ipAddresses.length === 0) {
      return res.status(500).json({ error: "No valid IPv4 addresses found." });
    }

    // Fetch Geolocation for each IP
    const geoData = await Promise.all(ipAddresses.map(getGeoLocation));

    res.json({ domain, route: geoData.filter(data => data !== null) });
  });
});

// 🌍 Function: Fetch IP Geolocation from ip-api.com (No API Key Required)
async function getGeoLocation(ip) {
  try {
    const response = await axios.get(`http://ip-api.com/json/${ip}`);
    const { lat, lon, city, regionName, country } = response.data;
    
    if (!lat || !lon) return null;

    return { ip, lat, lon, city, region: regionName, country };
  } catch (error) {
    console.error(`❌ Error fetching geolocation for ${ip}:`, error.message);
    return null;
  }
}

// 🔥 Start Server
app.listen(PORT, "0.0.0.0", () => {
  console.log(`🚀 Server running on http://0.0.0.0:${PORT}`);
});