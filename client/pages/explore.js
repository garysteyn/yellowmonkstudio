import {useState} from 'react';

function explore() {

        fetch("http://127.0.0.1:8000/creators/lol/", {
        method: 'GET',
      })

  return (
    <div>explore</div>
  )
}

export default explore