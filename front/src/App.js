import React, { Suspense } from 'react';
import { HashRouter, Route, Switch } from "react-router-dom";

import MainPage from './Components/MainPage/MainPage';
import Detail from './Components/Detail/Detail';
import Upload from './Components/Upload/Upload';
import Login from './Components/Login/Login';
import Register from './Components/Register/Register';


function App() {
  return (
    <div className="App">
      <HashRouter>
        <Switch>
          <Route exact path='/' component ={MainPage}/>
          <Route exact path='/detail' component ={Detail}/>
          {/* <Route exact path='/detail/:id' component ={Detail}/> */}
          <Route exact path='/upload' component ={Upload}/>
          <Route exact path='/login' component ={Login}/>
          <Route exact path='/register' component ={Register}/>
        </Switch>
      </HashRouter>
      
    </div>
  );
}

export default App;
