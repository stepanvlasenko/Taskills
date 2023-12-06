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
    return (
        <YMap {...props} location={{center: [longitude, latitude], zoom: 12}} mode="vector">
            <YMapDefaultSchemeLayer />
            <YMapDefaultFeaturesLayer />
            <YMapMarker coordinates={[longitude, latitude]} >
                <section className='map-marker'>
                    <div className='map-marker__description'>
                        <p className='map-marker__text text--roboto-700'>{title}</p>
                        <p className='map-marker__text text--roboto-700'>Адрес: {address}</p>
                    </div>
                    <img className='map-marker__image' src="/images/map-baloon.svg" />
                </section>
            </YMapMarker>
        </YMap>
    )
}