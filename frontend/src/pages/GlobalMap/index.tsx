import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import { useApi } from '../../assets/ts/useApi';

import './style.css'
import type { Sight } from '@types';
import MarkerBlock from '../../components/MarkerBlock';

const ymaps3Reactify = await ymaps3.import('@yandex/ymaps3-reactify');
const reactify = ymaps3Reactify.reactify.bindTo(React, ReactDOM);
const {YMap, YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer } = reactify.module(ymaps3)

export default function GlobalMap() {
    const [sights, setSights] = useState<Sight[]>([])
    const sightApi = useApi().useSightApi()

    useEffect(() => {
        sightApi.getAll().then((responce) => {
            if (!responce.status) {
                console.error(`Invalid responce. ${responce.data}`)
                return
            }
            setSights(() => (responce.data as Sight[]))
            return responce
        })
    }, [])
    
    return (
        <div className='global-map'>
            <div className='global-map__information'>
                <h2 className='global-map__title text--ibm-300'>Интерактивная карта</h2>
                <p className='global-map__text text--ibm-300'>Интерактивная карта со всеми достопримечательностями Волгоградской области. Нажмите на маркер, чтобы увидеть информацию.</p>
            </div>
            <div className='global-map__map>
                <YMap location={{center: [44.516975, 48.707067], zoom: 8}} mode="vector">
                    <YMapDefaultSchemeLayer />
                    <YMapDefaultFeaturesLayer />
                    {sights.map(v => <MarkerBlock key={v.id} title={v.title} address={v.address} latitude={v.latitude} longitude={v.longitude} isDefaultActive={false}/>)}
                </YMap>
            </div>
        </div>

    )
}
