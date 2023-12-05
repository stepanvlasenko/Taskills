import './style.css'

export default function Main() {

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
        </div>
    )
}