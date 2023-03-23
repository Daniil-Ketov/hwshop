import React from "react";
import Hardware from "./components/Hardware";
import { HeadlineCards } from "./components/HeadlineCards";
import Hero from "./components/Hero";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div>
      <Navbar />
      <Hero />
      <HeadlineCards />
      <Hardware />
    </div>
  );
}

export default App;
