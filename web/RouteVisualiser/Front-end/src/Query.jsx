import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { useState } from "react";

function TracerouteMap() {
  const [route, setRoute] = useState([]);

  async function traceRoute() {
    let target = document.querySelector("input").value;
  
    if (!target) {
      alert("Please enter a domain name!");
      return;
    }
  
    try {
      const response = await fetch("http://localhost:5000/traceroute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ domain: target }),
      });
  
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
  
      const data = await response.json();
      console.log("Traceroute Response:", data); // DEBUGGING
  
      if (!data.route || data.route.length === 0) {
        alert("No route data found!");
        return;
      }
  
      setRoute(data.route);
    } catch (error) {
      console.error("Error:", error);
      alert("Error fetching traceroute data");
    }
  }
  

  return (
    <div>
      <input type="text" placeholder="Enter Domain Name" />
      <button onClick={traceRoute}>Traceroute</button>

      {/* Map Component */}
      <MapContainer center={[20, 0]} zoom={2} style={{ height: "500px", width: "100%" }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {route.map((hop, index) => (
          <Marker key={index} position={[hop.latitude, hop.longitude]}>
            <Popup>
              <strong>IP:</strong> {hop.ip} <br />
              <strong>City:</strong> {hop.city} <br />
              <strong>Region:</strong> {hop.region} <br />
              <strong>Country:</strong> {hop.country}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default TracerouteMap;
