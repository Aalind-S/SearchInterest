import React,{useEffect} from 'react'
import Aos from 'aos';
import "aos/dist/aos.css"
import './NavBar.css'
import logo from '../NavBar/Vector8.png'
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import About from '../About/About'

function NavBar(){
  { useEffect(() => {
    Aos.init({duration:1000})
  },[])}
    const [movenav,setnavbar] =useState(false);

    const changeNav = () => {
      if(window.scrollY>=50){
        setnavbar(true);
      }
      else{
        setnavbar(false);
      }
    }

    window.addEventListener('scroll', changeNav)
return (<nav className={movenav?"design navbar navbar-expand-lg sticky-top":"design navbar navbar-expand-lg"}>
  <div data-aos="slide-down" className="container-fluid">
    <a className="navbar-brand col-lg-5 col-md-8 scope" href="#">Search Interest <img className='logo' src={logo}/></a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse row justify-content-center navbar-collapse fl cd " id="navbarNav">
      <ul className="navbar-nav ">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href={About}>About</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">Service</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="">Contact</a>
        </li >
        <li className="nav-item adjust">
        <a className="nav-link" href="">Log in</a>
        </li>
      </ul>
    </div>
  </div>
</nav>)
};

export default NavBar