import React, { Suspense } from 'react';
import { HashRouter, Route, Switch } from "react-router-dom";

import MainPage from './Components/MainPage/MainPage';
import Detail from './Components/Detail/Detail';
import Upload from './Components/Upload/Upload';


function App() {
  return (
    <div className="App">
      <HashRouter>
        <Switch>
          <Route exact path='/MainPage' component ={MainPage}/>
          <Route exact path='/detail' component ={Detail}/>
          {/* <Route exact path='/detail/:id' component ={Detail}/> */}
          <Route exact path='/upload' component ={Upload}/>
        </Switch>
      </HashRouter>
      
    </div>
  );
}

export default App;
