import React, { useState } from "react";
import TracerouteForm from "./components/TracerouteForm";
import MapComponent from "./components/MapComponent";

function App() {
  const [route, setRoute] = useState([]);

  return (
    <div>
      <h1>Traceroute Network Visualization</h1>
      <TracerouteForm setRoute={setRoute} />
      <MapComponent route={route} />
    </div>
  );
}

export default App;
