import React from 'react'
import ReactDOM from 'react-dom';
import './style.css'
import MarkerBlock from '../MarkerBlock';

const ymaps3Reactify = await ymaps3.import('@yandex/ymaps3-reactify');
const reactify = ymaps3Reactify.reactify.bindTo(React, ReactDOM);
const {YMap, YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer } = reactify.module(ymaps3)

interface SightMapProps {
    title: string
    address: string
    latitude: number
    longitude: number
}

export default function SightMap({title, address, latitude, longitude, ...props}: SightMapProps) {
    return (
        <YMap {...props} location={{center: [longitude, latitude], zoom: 12}} mode="vector">
            <YMapDefaultSchemeLayer />
            <YMapDefaultFeaturesLayer />
            <MarkerBlock title={title} address={address} latitude={latitude} longitude={longitude} isDefaultActive={true}/>
        </YMap>
    )
}