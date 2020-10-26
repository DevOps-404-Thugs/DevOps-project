import React, { Suspense } from 'react';
import { BrowserRouter, Route, Switch } from "react-router-dom";

import MainPage from './Components/MainPage/MainPage';
import Detail from './Components/Detail/Detail';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path='/MainPage' component ={MainPage}/>
          <Route exact path='/detail' component ={Detail}/>
        </Switch>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
