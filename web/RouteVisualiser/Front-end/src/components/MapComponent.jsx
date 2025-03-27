import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

function MapComponent({ route }) {
  const defaultPosition = [20.5937, 78.9629]; // Default: India

  return (
    <MapContainer center={defaultPosition} zoom={3} style={{ height: "500px", width: "100%" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

      {route.length > 0 ? (
        route
          .filter(point => point.lat !== undefined && point.lon !== undefined) // ✅ Filter out undefined values
          .map((point, index) => (
            <Marker key={index} position={[point.lat, point.lon]}>
              <Popup>
                <strong>{point.ip}</strong> <br />
                {point.city}, {point.region}, {point.country}
              </Popup>
            </Marker>
          ))
      ) : (
        <p>Loading data...</p>
      )}
    </MapContainer>
  );
}

export default MapComponent;
