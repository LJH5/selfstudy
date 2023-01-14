import React from 'react'
import './App.css';


function Left1(props) {
  return (
    <div>
      <h1>Left1</h1>
    </div>
  )
}

function App() {
  return (
    <div className="App" id='container'>
      <h1>Root</h1>
      <Left1 />
    </div>
  );
}

export default App;
