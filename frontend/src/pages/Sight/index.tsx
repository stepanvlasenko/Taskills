import { useParams } from 'react-router-dom'
import { useApi } from '../../assets/ts/useApi'
import { useEffect, useState } from 'react'
import './style.css'
import type { Sight } from '@types'
import SightMap from '../../components/SightMap'

export default function Sight() {
    const [sight, setSight] = useState<Sight>()
    const sightApi = useApi().useSightApi()
    const params = useParams()

    const id = +(params.id || 0)
    useEffect(() => {
        sightApi.get(id).then((responce) => {
            if (!responce.status) {
                console.error(`Invalid responce. ${responce.data}`)
                return
            }
            setSight(responce.data as Sight)
            return responce
        }) 
    }, [])
    if (!sight) return (<></>)
    return (
        <>
            <div className='sight'>
                <div className='sight__container'>
                    <img className='sight__main-image' src={sight.images[0]} alt={sight.title} />
                    <div className='sight__information'>
                        <h2 className='sight__title text--ibm-400'>{sight.title}</h2>
                        <p className='sight__description text--roboto-400'>{sight.description}</p>
                        <h3 className='sight__subtitle text--ibm-400'>Адрес:</h3>
                        <p className='sight__address text--roboto-400'>{sight.address}</p>
                    </div>
                </div>
                <div className='sight__map'><SightMap title={sight.title} address={sight.address} latitude={sight.latitude} longitude={sight.longitude}/></div>
            </div>
            <div className='sight-images'>
                {sight.images.map((v, i) => (
                    <img key={i} src={v}/>
                ))}
            </div>
        </>

    )
}