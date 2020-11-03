import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Axios from 'axios'
import "./NavBar.css"

function NavBar() {
	const [loginState, setLoginState] = useState(0);//default as unlogin

	useEffect(() => {
		Axios.get(`http://127.0.0.1:8000/account`)
		.then(response => {
			console.log("accountGET:"+response.status)
			console.log(response)
			if(response.status === 200){
				setLoginState(1)//unlogin
				console.log("loginState after account200:" + loginState);
			}
		})
		.catch(function(error){
			console.log("accountGET:"+error.response.status)
			console.log(error.response)
			if(error.response.status === 405){
				setLoginState(0)//logined
				console.log("loginState after account405:" + loginState);
			}
		})

		console.log("loginState:" + loginState);
	},[]);


	const onLogout = (event) => {
		Axios.get(`http://127.0.0.1:8000/logout`)
		.then(response => {
			console.log("logoutGET:"+response.status)
			console.log(response)
			if(response.status === 200){
				setLoginState(0)//unlogin
				console.log("loginState after logout200:" + loginState);
			}
		})
		.catch(function(error){
			console.log("logoutGET:"+error.response.status)
			console.log(error.response)
			console.log("loginState:" + loginState);
		})
	}

  return (
    <nav class="menu">
			<div class="menu_container">
				<div class="menu_right">
					{/* {loginState === 0? */}
						<Link class="link" to={'/login'} visible={!loginState}>Login</Link>
						{/* : */}
						<button class="btn btn-primary" visible={loginState} onClick={onLogout}>log out</button> 
					{/* } */}
						
				</div>
			</div>
    </nav>
  )
}

export default NavBar