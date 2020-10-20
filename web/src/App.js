import React from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.svg';
import './App.css';
import Detail from './Detail';

function DetailLink() {
  function handleClick(e) {
    ReactDOM.render(
      <React.StrictMode>
        <Detail />
      </React.StrictMode>,
      document.getElementById('root')
    );
  }

  return (
    <button onClick={handleClick}>
      Detail
    </button>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <DetailLink />
      </header>
      
    </div>
  );
}

export default App;
