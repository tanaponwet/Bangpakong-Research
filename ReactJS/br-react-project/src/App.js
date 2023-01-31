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

import React, { createContext, useState } from 'react'
import './App.css';
import NavigationBar from './components/NavigationBar';
import CurrentForecast from './components/CurrentForecast';
import HourForecast from './components/HourForecast';
import HourForecastCard from './components/HourForecastCard';
import Footer from './components/Footer';
import MapBox from './components/MapBox';

export const ThemeContext = createContext(null)

function App() {

  const [theme, setTheme] = useState('light');

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
            <CurrentForecast />
            <HourForecast />
            <MapBox />
          </div>
        </div>
        <Footer />
      </div>
    </ThemeContext.Provider>
  )
}

export default App
