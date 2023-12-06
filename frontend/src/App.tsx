import './App.css'

import { Outlet } from 'react-router-dom'
import Footer from './components/Footer'
import Header from './components/Header'

export default function App() {
    return (
        <div className='app'>
            <Header />
            <Outlet />
            <Footer />
        </div>
    )
}