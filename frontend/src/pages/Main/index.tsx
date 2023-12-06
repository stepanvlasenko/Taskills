import { useEffect, useState } from 'react'
import './style.css'
import { Sight } from '@types'
import { useApi } from '../../assets/ts/useApi'
import SightCard from '../../components/SightCard'

export default function Main() {
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
        <div className='main'>
            <div className='main__promo promo'>
                <div className='promo__title'>
                    <div className='promo-title__text text--ibm-200'>Туристические места</div>
                    <div className='promo-title__text text--ibm-200'><span className='promo-title__span text--ibm-400'>Волгоградской</span> области</div>
                </div>
                <div className='promo__content'>
                    <p className='promo__text text--roboto-400'>Сборник мест для посещения <span className='text--red'>туристам</span> Волгоградской области</p>
                    <img className='promo__image' src="/images/volgograd.webp" alt="Волгоградская область" />
                </div>
            </div>
            <div className='main__sights'>
                <h1 className='main-sights__title text--ibm-200'>Места для посещения</h1>
                <div className='sights'>
                    {sights.length > 0 ? sights.map((v) => (
                        <SightCard key={v.id} title={v.title} id={v.id} image={v.images[0]} description={v.description} />
                    )) : (<></>)}
                </div>
            </div>
        </div>
    )
}