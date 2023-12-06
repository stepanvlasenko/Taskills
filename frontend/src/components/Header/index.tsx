import { Link } from 'react-router-dom'
import './style.css'

export default function Header(){
    return(
        <header className='header'>
            <div className="header__left">
                <Link to={'/'} className='header__link'>
                    Места
                </Link>
            </div>
            <div className="header__center">
                <img src="/images/logo.svg" alt="" className='header__logo'/>
            </div>
            <div className="header__right">
                <Link to={'/about'} className='header__link'>
                    О проекте
                </Link>
            </div>
        </header>
    )
}