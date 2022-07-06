import React from 'react'
import './NavBar.css'
import { FaBars } from 'react-icons/fa';
import { IoIosClose } from 'react-icons/io';
const NavBar= () =>{
const [toggleMenu, setToggleMenu] = React.useState(false);
return (
  <nav className='web_navbar'>
    <div className='title'>
      <h1>Search Interest</h1>
    </div>
    <ul className='app_navbar-links'>
      <li className='heading'><a className='heading' href='#'>Home</a></li>
      <li className='heading'><a className='heading' href='#'>About</a></li>
      <li className='heading'><a className='heading' href='#'>Service</a></li>
      <li className='heading'><a className='heading' href='#'>contact</a></li>
    </ul>
    <div>
      <a href="#login"className='app_login heading'>Log in</a>
    </div>
    <div className="app__navbar-smallscreen">
        <FaBars onClick={() => setToggleMenu(true)} />
        {toggleMenu && (
          <div className="app__navbar-smallscreen_overlay flex__center slide-bottom ">
              <IoIosClose className="overlay__close" onClick={() => setToggleMenu(false)} />
            <ul className="app__navbar-smallscreen_links">
              <li><a className='heading1' href="#home" onClick={() => setToggleMenu(false)}>Home</a></li>
              <li><a className='heading1' href="#about" onClick={() => setToggleMenu(false)}>About</a></li>
              <li><a className='heading1' href="#menu" onClick={() => setToggleMenu(false)}>Service</a></li>
              <li><a className='heading1' href="#awards" onClick={() => setToggleMenu(false)}>contact</a></li>
              <li><a className='heading1' href="#awards" onClick={() => setToggleMenu(false)}>Log in</a></li>
            </ul>
          </div>
        )}
      </div>
  </nav>
);
};

export default NavBar