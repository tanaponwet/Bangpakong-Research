import React, { Component } from 'react'
import '../styles/CurrentForecast.css'
import BlueSaltWater from '../icons/salt-water/03/blue-salt-water.png'
import YellowSaltWater from '../icons/salt-water/03/yellow-salt-water.png'
import RedSaltWater from '../icons/salt-water/03/red-salt-water.png'
import HomeWorkRoundedIcon from '@mui/icons-material/HomeWorkRounded';
import LocationOnRoundedIcon from '@mui/icons-material/LocationOnRounded';
import WaterRoundedIcon from '@mui/icons-material/WaterRounded';
import MapRoundedIcon from '@mui/icons-material/MapRounded';
import OpacityRoundedIcon from '@mui/icons-material/OpacityRounded';
import ElectricBoltRoundedIcon from '@mui/icons-material/ElectricBoltRounded';
import WatchLaterRoundedIcon from '@mui/icons-material/WatchLaterRounded';
import { HourglassEmpty } from '@mui/icons-material';

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

function CurrentForecast(props) {
    const {data} = props; //same as -> const data = props.data;
    // console.log("Data in CurrentForecast:", data);
    return (
        // <div>CurrentForecast</div>
        <main className="current-forecast">
            
            <div className="header">
                <div className="title-1">
                    <HomeWorkRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-1'>หน้าวัดคลองเขื่อน</p>
                </div>
            </div>
            <div className="header">
                <div className="title-2">
                    <LocationOnRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-2'>ตำบล คลองเขื่อน อำเภอ คลองเขื่อน ฉะเชิงเทรา</p>
                </div>
                <div className="title-2">
                    <WaterRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-2'>ระยะห่างจากทะเล 86 กม.</p>
                </div>
                <div className="title-2">
                    <MapRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <a className='link-text' href="https://goo.gl/maps/rhut5YAiXzS17DCw6" target='_blank'>13°45'39.3"N, 101°11'36.0"E</a>
                </div>
            </div>
            <div className="info">
                <div className="info-con">
                    <div className="salinity-con">
                        <div className="title-1">
                            <OpacityRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                            <p className='text-2'>ความเค็ม</p>
                        </div>
                        <div className="salinity-info">
                            {/* <p className='salinity-value'>99.99</p> */}
                            <p className='salinity-value'>{data.gl}</p>
                            <p className='salinity-unit'>g/l</p>
                        </div>
                    </div>
                    <div className="ec-con">
                        <div className="title-1">
                            <ElectricBoltRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                            <p className='text-2'>ค่าการนำไฟฟ้า</p>
                        </div>
                        <div className="ec-info">
                            {/* <p className='ec-value'>99999.99</p> */}
                            <p className='ec-value'>{data.uscm}</p>
                            <p className='ec-unit'>µS/cm</p>
                        </div>
                    </div>
                </div>

                <figure className="img-con">
                    {/* <img src={BlueSaltWater} alt="" /> */}
                    <img src={mapImg(data.gl)} alt="" />

                </figure>
            </div>
            <div className="footer">
                <div className="title-1">
                    <WatchLaterRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    {/* <p className='text-1'>ศ. 00/00/0000 00:00 GMT+07:00</p> */}
                    <p className='text-1'>{data.date} {data.time} GMT+07:00</p>
                </div>
            </div>
        </main>
    )
}

export default CurrentForecast