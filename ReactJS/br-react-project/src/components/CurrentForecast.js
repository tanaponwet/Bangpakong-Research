import React from 'react'
import '../styles/CurrentForecast.css'
import BlueSaltWater from '../icons/salt-water/03/blue-salt-water.png'
// import YellowSaltWater from '../icons/salt-water/03/yellow-salt-water.png'
// import RedSaltWater from '../icons/salt-water/03/red-salt-water.png'
import HomeWorkRoundedIcon from '@mui/icons-material/HomeWorkRounded';
import LocationOnRoundedIcon from '@mui/icons-material/LocationOnRounded';
import WaterRoundedIcon from '@mui/icons-material/WaterRounded';
import MapRoundedIcon from '@mui/icons-material/MapRounded';
import OpacityRoundedIcon from '@mui/icons-material/OpacityRounded';
import ElectricBoltRoundedIcon from '@mui/icons-material/ElectricBoltRounded';
import WatchLaterRoundedIcon from '@mui/icons-material/WatchLaterRounded';

function CurrentForecast() {
    return (
        // <div>CurrentForecast</div>
        <main className="current-forecast">
            <div className="header">
                <div className="title-1">
                    <HomeWorkRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <span className='text-1'>สถานีชลประทานฉะเชิงเทรา</span>
                </div>
            </div>
            <div className="header">
                <div className="title-2">
                    <LocationOnRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-2'>ต.คลองบ้านโพธิ์ อ.บ้านโพธิ์ จ.ฉะเชิงเทรา</p>
                </div>
                <div className="title-2">
                    <WaterRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-2'>ระยะห่างจากทะเล 35 กม.</p>
                </div>
                <div className="title-2">
                    <MapRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <a className='link-text' href="https://www.google.co.th/maps/place/13%C2%B035'00.3%22N+101%C2%B004'15.1%22E/@13.5834272,101.0686713,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x933e0bbbd1d32142!8m2!3d13.583422!4d101.07086?hl=th" target='_blank'>13.583422, 101.07086</a>
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
                            <p className='salinity-value'>99.99</p>
                            <p className='salinity-unit'>g/l</p>
                        </div>
                    </div>
                    <div className="ec-con">
                        <div className="title-1">
                            <ElectricBoltRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                            <p className='text-2'>ค่าการนำไฟฟ้า</p>
                        </div>
                        <div className="ec-info">
                            <p className='ec-value'>99999.99</p>
                            <p className='ec-unit'>µS/cm</p>
                        </div>
                    </div>
                </div>
                <figure className="img-con">
                    <img src={BlueSaltWater} alt="" />
                </figure>
            </div>
            <div className="footer">
                <div className="title-1">
                    <WatchLaterRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-1'>ศ. 00/00/0000 00:00 GMT+07:00</p>
                </div>
            </div>
        </main>
    )
}

export default CurrentForecast