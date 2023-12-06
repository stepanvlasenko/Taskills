import './style.css'

export default function Footer(){

    return(
        <div className='footer'>
            <div className='footer__about'>
                <p className='footer__heading text--ibm-300'>О проекте</p>
                <div className='footer__text text--roboto-400'>
                    Приложение поможет вам узнать о туристических местах Волгоградской области и составить свой маршрут для путешествия. Для этого вы можете воспользоваться списком всех достопримечательностей и интерактивной картой туристических мест. На странице каждой достопримечательности присутствуют описание и фотографии для ознакомления, а также адрес и расположение на карте.
                </div>
            </div>
            <div className='footer__vertical-line'></div>
            <div className='footer__developers'>
                <p className='footer__heading text--ibm-300'>Разработчики</p>
                <ul className='footer__list'>
                   <li className='footer__text text--roboto-400'>Власенко Степан</li> 
                   <li className='footer__text text--roboto-400'>Доманов Фёдор</li>
                </ul>
            </div>
        </div>
    )
}