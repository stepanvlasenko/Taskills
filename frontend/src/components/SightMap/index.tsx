import React from 'react'
import ReactDOM from 'react-dom';
import './style.css'

const ymaps3Reactify = await ymaps3.import('@yandex/ymaps3-reactify');
const reactify = ymaps3Reactify.reactify.bindTo(React, ReactDOM);
const {YMap, YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer, YMapMarker } = reactify.module(ymaps3)

interface SightMapProps {
    title: string
    address: string
    latitude: number
    longitude: number
}

export default function SightMap({title, address, latitude, longitude, ...props}: SightMapProps) {
    console.log(ymaps3)
    return (
        <YMap location={{center: [longitude, latitude], zoom: 16}} mode="vector">
            <YMapDefaultSchemeLayer />
            <YMapDefaultFeaturesLayer />
            <YMapMarker coordinates={[longitude, latitude]} >
                <img className='map__marker' src="/images/map-baloon.svg" />
            </YMapMarker>
        </YMap>
    )
}