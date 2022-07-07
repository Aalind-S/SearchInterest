import React from 'react'

function Details(props) {
  return (
    <div className='col-lg-6 col-md-6'>
        <div className="card" >
  <img src={'.'} className="card-img-top" alt="..." />
  <div className="card-body">
    <h5 className="card-title">{props.title}</h5>
    <p className="card-text">{props.detail}</p>
    <a href="#" className="btn btn-primary">Go somewhere</a>
  </div>
</div>
    </div>
  )
}

export default Details