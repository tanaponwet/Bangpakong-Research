import React from 'react'
import Map, {
    Marker,
    NavigationControl,
    FullscreenControl,
    GeolocateControl,
} from "react-map-gl";
import '../styles/MapBox.css';
import 'mapbox-gl/dist/mapbox-gl.css';
import LocationOnRoundedIcon from '@mui/icons-material/LocationOnRounded';

function MapBox() {
    return (
        <main className="map-box">
            <div className="header">
                <div className="title-1">
                    <LocationOnRoundedIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-1'>ตำแหน่งสถานี</p>
                </div>
            </div>
            <div className="map-con">
                <Map
                    mapboxAccessToken="pk.eyJ1Ijoiam9lY2VrbWl0bCIsImEiOiJjbGRsdmVpMGEwMmk1NDFuMGFpdnV6NWl2In0.oyKImg2FLZ0ZemRrSWDhgA"
                    initialViewState={{
                        longitude: 101.1933062372916,
                        latitude: 13.761010528753618,
                        zoom: 15
                    }}
                    style={{
                        width: '100%',
                        height: '100%',
                        borderRadius: '8px',
                    }}             
                    mapStyle="mapbox://styles/mapbox/streets-v12"
                >
                    <Marker longitude='101.1933062372916' latitude='13.761010528753618' color='red' />
                    <NavigationControl position='bottom-right' />
                    <FullscreenControl position='bottom-right'/>
                    <GeolocateControl position='bottom-right'/>
                </Map>
                {/* <div className="rectangle"></div> */}
            </div>
        </main>
    )
}

export default MapBox