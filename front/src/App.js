import React from 'react';
import { HashRouter, Route, Switch } from "react-router-dom";

import NavBar from './Components/NavBar/NavBar';
import MainPage from './Components/MainPage/MainPage';
import Detail from './Components/Detail/Detail';
import Upload from './Components/Upload/Upload';
import Login from './Components/Login/Login';
import Register from './Components/Register/Register';
import Account from './Components/Account/Account';
import AccountUpdate from './Components/AccountUpdate/AccountUpdate';


function App() {
  return (
    <div className="App">
      <HashRouter>
        <NavBar />
        <Switch>
          <Route exact path='/' component ={MainPage}/>
          <Route exact path='/detail' component ={Detail}/>
          {/* <Route exact path='/detail/:id' component ={Detail}/> */}
          <Route exact path='/upload' component ={Upload}/>
          <Route exact path='/login' component ={Login}/>
          <Route exact path='/register' component ={Register}/>
          <Route exact path='/account' component ={Account}/>
          <Route exact path='/account_update' component ={AccountUpdate}/>
        </Switch>
      </HashRouter>
      
    </div>
  );
}

export default App;
