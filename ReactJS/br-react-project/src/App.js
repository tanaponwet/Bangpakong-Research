// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

<<<<<<< Updated upstream
import React, { createContext, useEffect, useState } from 'react'
=======
import React, { createContext, useState, useEffect } from 'react'
>>>>>>> Stashed changes
import './App.css';
import NavigationBar from './components/NavigationBar';
import CurrentForecast from './components/CurrentForecast';
import HourForecast from './components/HourForecast';
import HourForecastCard from './components/HourForecastCard';
import Footer from './components/Footer';
import MapBox from './components/MapBox';

export const ThemeContext = createContext(null)

function App() {

  const [hourly, passHourly] = useState([]);

  const [theme, setTheme] = useState('light');
  const [hourly, setHourly] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000", {
      "methods":"GET",
      headers: {
        "Content-Type":"applications/json"
      }
    })
    .then(resp => resp.json())
    .then(resp => setHourly(resp))
    .catch(error => console.log(error))
  })

  const toggleTheme = (state) => {
    if (state === true) {
      setTheme('dark')
    } else if (state === false) {
      setTheme('light')
    }
  }

  useEffect(() => {
    fetch("http://127.0.0.1:5000", {
      "methods":"GET",
      headers: {
        "Content-Type":"applications/json"
      }
    })
    .then(resp => resp.json())
    // .then(resp => console.log(resp))
    .then(resp => passHourly(resp))
    .catch(error => console.log(error))


  },[])

  return (
    // <div>App</div>
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div className='App' id={theme}>
        <NavigationBar onToggleTheme={toggleTheme} />
        <div className="card-list">
          <div className="card-con">
<<<<<<< Updated upstream
            <CurrentForecast data ={hourly}/>
=======
            <CurrentForecast hourly = {hourly}/>
>>>>>>> Stashed changes
            <HourForecast />
            <MapBox />
          </div>
        </div>
        {/* <NavigationBar onToggleTheme={toggleTheme} /> */}
        <Footer />
      </div>
    </ThemeContext.Provider>
  )
}

export default App
