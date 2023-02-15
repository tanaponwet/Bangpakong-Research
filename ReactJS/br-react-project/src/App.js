import React, { createContext, useEffect, useState } from 'react'
import './App.css';
import NavigationBar from './components/NavigationBar';
import CurrentForecast from './components/CurrentForecast';
import HourForecast from './components/HourForecast';
import HourForecastCard from './components/HourForecastCard';
import Footer from './components/Footer';
import MapBox from './components/MapBox';
import socketIOClient from "socket.io-client";
// import Graph from "./components/Graph";

export const ThemeContext = createContext(null)




function App() {

  const [theme, setTheme] = useState('light');

  const [data, setData] = useState({ current: {} });

  const socket = socketIOClient("http://127.0.0.1:5000/hourly");


  useEffect(() => {
    fetch("http://127.0.0.1:5000/", {
      headers: {
        "Content-Type": "application/json",
      }
    })
    .then(response => response.json())
    .then(data => setData(data))
  }, []);


  useEffect(() => {
    socket.on("post_hourly", (data) => {
      setData(JSON.parse(data));
      // const parsedData = JSON.parse(data);
      // console.log("Hourly Data:", parsedData);
      // setData(parsedData);
    });
    return () => {
      socket.off("post_hourly");
    };
  });


  const toggleTheme = (state) => {
    if (state === true) {
      setTheme('dark')
    } else if (state === false) {
      setTheme('light')
    }
  }

  return (
    // <div>App</div>
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div className='App' id={theme}>
        <NavigationBar onToggleTheme={toggleTheme} />
        <div className="card-list">
          <div className="card-con">
            <CurrentForecast data={data.current} />
            <HourForecast />
            {/* <Graph /> */}
            <MapBox />
          </div>
        </div>
        <Footer />
      </div>
    </ThemeContext.Provider>
  )
}

export default App
