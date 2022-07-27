import React,{useState,useEffect} from 'react'
import Aos from "aos"
import "aos/dist/aos.css"
import Content from './Content'
import Print from './Print'
import backimg from './Ellipse28.png'
import './About.css'
function About() {
    useEffect(() => {
      Aos.init({duration:2000})
    },[])
  function cont(data){

    return (
      <Print
      title={data.title}
      info={data.detail}
      />
    )
  }
  return (
    <div>
      <div>
      <img data-aos="slide-up" className="back" src={backimg} />
      </div>
      <div data-aos="slide-up" className='row flow'>
        {Content.map(cont)}
      </div>
    </div>
  )
}

export default About