import React, { useState } from 'react'
import ReactDOM from 'react-dom';
import './style.css'

interface MarkerBlockProps {
    latitude: number
    longitude: number
    title: string
    address: string
    isDefaultActive?: boolean
}

const ymaps3Reactify = await ymaps3.import('@yandex/ymaps3-reactify');
const reactify = ymaps3Reactify.reactify.bindTo(React, ReactDOM);
const { YMapMarker } = reactify.module(ymaps3)

export default function MarkerBlock({latitude, longitude, title, address, isDefaultActive = false, ...props}: MarkerBlockProps) {
    const [isActive, setIsActive] = useState(isDefaultActive)

    return (
        <YMapMarker {...props} coordinates={[longitude, latitude]} >
            <section className='map-marker'>
                <img onClick={() => setIsActive((v) => !v)} className='map-marker__image' src="/images/map-baloon.svg" />
                {!isActive ? <></> : (
                    <div className='map-marker__description'>
                        <p className='map-marker__title text--ibm-400'>{title}</p>
                        <p className='map-marker__address text--roboto-400'>Адрес: {address}</p>
                    </div>
                )}
                
            </section>
        </YMapMarker>
    )
}