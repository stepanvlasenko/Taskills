import './style.css'

export default function Footer(){

    return(
        <div className='footer'>
            <div className='footer__about'>
                <p className='footer__heading text--ibm-300'>О проекте</p>
                <div className='footer__text text--roboto-400'>
                    {/* Вставить инфу о проекте */}
                    Lorem ipsum dolor sit amet consectetur. Arcu sed massa vel porta in ut a porta. Ultrices adipiscing eget tincidunt amet tincidunt. Nunc turpis sagittis molestie nunc ac in. Convallis donec tellus hendrerit dui praesent proin arcu porttitor velit. A sed porttitor elementum interdum venenatis tristique. Euismod consequat nibh eget odio. Etiam pellentesque tortor vestibulum at et at lectus. Habitasse faucibus diam vel et ipsum nisi tellus bibendum. Senectus auctor adipiscing orci gravida. Netus posuere maecenas sed purus. Non ac neque blandit sed in. Commodo ultricies malesuada tempus purus suspendisse sed leo. Sit feugiat fermentum in nibh malesuada viverra.
                </div>
            </div>
            <div className='footer__vertical-line'></div>
            <div className='footer__developers'>
                <p className='footer__heading text--ibm-300'>Разработчики</p>
                <ul className='footer__list'>
                   <li className='footer__text text--roboto-400'>Власенко Степан </li> 
                   <li className='footer__text text--roboto-400'>Доманов Фёдор </li>
                   <li className='footer__text text--roboto-400'>Ткаченко Егор</li>
                </ul>
            </div>
        </div>
    )
}