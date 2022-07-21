import React from 'react'
import Content from './Content'
import './About.css'
import Details from './Details'
function About() {
  return (
  <div className='container mb-5'>
    <div className='row'>
        <div className='col-lg-12 mb-aut0'>
        <div className='row gy-5'>
    {
        Content.map((val,ind) =>{
            return <Details
            key={val.title}
            title={val.title}
            detail={val.detail}/>
        } )
    }
    </div>
    </div>
    </div>
  </div>    
  )
}

export default About