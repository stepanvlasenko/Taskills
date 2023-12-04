import './App.css'
import SightCard from './components/SightCard'
import SightMap from './components/SightMap'

export default function App() {
  return (
    <div className='app-test'>
      <SightCard title='Водопад Архангела' id={1} image='https://www.smy.travel/ru/wp-content/uploads/sites/5/2020/06/waterfall.jpg' description='Порой кажется, что природа некоторых мест будто взята из фантастической сказки. Ведь на нашей Земле есть столько потрясающих и неописуемых мест с их магическими пейзажами, которые просто необходимо увидеть хотя бы раз в жизни. Примером служат захватывающие дух водопады, падающие каскадами на тысячи метров, что представляет удивительное зрелище. И несмотря на то, что на планете можно встретить множество разных водопадов, мы решили выделить из них 9 наиболее уникальных.'/>
    </div>
  )
}