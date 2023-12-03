import './App.css'
import SightMap from './components/SightMap'

export default function App() {
  return (
    <div className='app-test'>
      <SightMap title='Test' address='There' latitude={50.200203} longitude={39.540543}/>
    </div>
  )
}