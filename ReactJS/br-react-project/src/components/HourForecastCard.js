import React from 'react'
import '../styles/HourForecastCard.css'
import BlueSaltWater from '../icons/salt-water/03/blue-salt-water.png'
// import YellowSaltWater from '../icons/salt-water/03/yellow-salt-water.png'
// import RedSaltWater from '../icons/salt-water/03/red-salt-water.png'

function HourForecastCard() {
    return (
        // <div>HourForecastCard</div>
        <main className="hour-forecast-card">
            <p className='date-text'>00/00/0000</p>
            <p className='time-text'>00:00</p>
            <figure className="img-con">
                <img src={BlueSaltWater} alt="" />
            </figure>
            <div className="salinity-info">
                <p className='salinity-value'>99.99</p>
                <p className='salinity-unit'>g/l</p>
            </div>
            <div className="ec-info">
                <p className='ec-value'>99999.99</p>
                <p className='ec-unit'>µS/cm</p>
            </div>
        </main>
    )
}

export default HourForecastCard