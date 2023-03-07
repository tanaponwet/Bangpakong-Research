import React from 'react'
import '../styles/HourForecastCard.css'
import BlueSaltWater from '../icons/salt-water/03/blue-salt-water.png'
import YellowSaltWater from '../icons/salt-water/03/yellow-salt-water.png'
import RedSaltWater from '../icons/salt-water/03/red-salt-water.png'

function roundTo(n, place) {    
    return +(Math.round(n + "e+" + place) + "e-" + place);
}

function mapImg(value) {
    const roundedValue = roundTo(value, 2);
    if (roundedValue <= .25){
        return BlueSaltWater;
    }
    else if(roundedValue <= 2){
        return YellowSaltWater;
    }
    else{
        return RedSaltWater;
    }
}

function HourForecastCard(props) {
    const {data} = props;
    return (
        // <div>HourForecastCard</div>
        <main className="hour-forecast-card">
            <p className='date-text'>{data.date}</p>
            <p className='time-text'>{data.time}</p>
            <figure className="img-con">
                {/* <img src={BlueSaltWater} alt="" /> */}
                <img src={mapImg(data.gl)} alt="" />
            </figure>
            <div className="salinity-info">
                <p className='salinity-value'>{data.gl}</p>
                <p className='salinity-unit'>g/l</p>
            </div>
            <div className="ec-info">
                <p className='ec-value'>{data.uscm}</p>
                <p className='ec-unit'>µS/cm</p>
            </div>
        </main>
    )
}

export default HourForecastCard