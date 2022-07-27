import React,{useState,useEffect} from 'react'
import { useSpring, animated,config } from 'react-spring'
import ellipse from '../Home/Ellipse1.png'
import Aos from 'aos';
import "aos/dist/aos.css"
import logo2 from '../Home/logo.png'
import './home.css'
function Home() {
  const [flip, set] = useState(false)
  const props = useSpring({
    to: { opacity: 1 },
    from: { opacity: 0 },
    reset: true,
    reverse: flip,
    delay: 550,
    config: config.molasses,
  })
  { useEffect(() => {
    Aos.init({duration:2000})
  },[])}
  return (
    <div>
      <div className='home-intro'>
        <animated.h1 style={props}>FIND INTEREST RATES IN<br/>ONE PLACE.</animated.h1>
      </div>
      <div className='circle'>
       <img data-aos="slide-up" className='elli' src={ellipse} />
       <img data-aos="slide-up" className='logo2' src={logo2} />
      </div>

    </div>
  )
}

export default Home