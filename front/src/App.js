import React, { Suspense } from 'react';
import { BrowserRouter, Route, Switch } from "react-router-dom";

import MainPage from './Components/MainPage/MainPage';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path='/MainPage' component ={MainPage}/>
        </Switch>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
