import React from 'react'
import './NavBar.css'
import { FaBars } from 'react-icons/fa';
import { IoIosClose } from 'react-icons/io';
import 'bootstrap/dist/css/bootstrap.min.css';
const NavBar= () =>(
 <nav className="navbar navbar-expand-lg">
  <div className="container-fluid">
    <a className="navbar-brand col-lg-7" href="#">Search Interest</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse cd" id="navbarNav">
      <ul className="navbar-nav col-lg">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">About</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">Service</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">Contact</a>
        </li>
      </ul>
      <a className="nav-item nav-link adjust" href="">Log in</a>
    </div>
  </div>
</nav>
);

export default NavBar