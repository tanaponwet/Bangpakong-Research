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

const pos = [
    {
        name: "meter",
        latitude: 101.1933062372916,
        longitude: 13.761010528753618,
        color: "red"
    },
    {
        name: "tmd (กรมอุตุ ฉะเชิงเทรา)",
        latitude: 101.458333,
        longitude: 13.515556,
        color: "blue"
    },
    {
        name: "cholpratan-bangkla",
        latitude: 101.164386,
        longitude: 13.695572,
        color: "cyan"
    },
    {
        name: "BPK003-bangnampriew",
        latitude: 101.14574452538852,
        longitude: 13.8703068398621, 
        color: "blue"
    },
    {
        name: "BPK001-bangpakong",
        latitude: 101.00111585309776,
        longitude: 13.549009362912644, 
        color: "blue"
    }
];


function MapBox() {
    const markers = pos.map((marker, index) => (
        <Marker
            key={index}
            longitude={marker.latitude}
            latitude={marker.longitude}
            color={marker.color}
        />
    ));

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
                        zoom: 9
                    }}
                    style={{
                        width: '100%',
                        height: '100%',
                        borderRadius: '8px',
                    }}
                    mapStyle="mapbox://styles/mapbox/streets-v12"
                >

                    {markers}
                    <NavigationControl position='bottom-right' />
                    <FullscreenControl position='bottom-right' />
                    <GeolocateControl position='bottom-right' />
                </Map>
                {/* <div className="rectangle"></div> */}
            </div>
        </main>
    )
}

export default MapBox