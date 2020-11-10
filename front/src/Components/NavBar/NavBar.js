import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Axios from 'axios'
import "./NavBar.css"


function NavBar() {
	const [loginState, setLoginState] = useState(0);//default as unlogin

	useEffect(() => {
		Axios.get(`http://127.0.0.1:8000/login`,{withCredentials: true})
		.then(response => {
			console.log("loginGET:"+response.status)
			console.log(response)
			if(response.status === 200){
				//console.log("loginState loginGET200:" + loginState);
				setLoginState(1)//unlogin
				//console.log("loginState after loginGET200:" + loginState);
			}else if(response.status === 205){
				setLoginState(0)//unlogin
				//console.log("loginState after loginGET205:" + loginState);
			}
		})
		// .catch(function(error){
		// 	console.log("loginGET:"+error.response.status)
		// 	console.log(error.response)
			
		// })

		console.log("loginState:" + loginState);
	},[]);
	

	const onLogout = (event) => {
		Axios.get(`http://127.0.0.1:8000/logout`, {withCredentials: true})
		.then(response => {
			console.log("logoutGET:"+response.status)
			console.log(response)
			if(response.status === 200){
				setLoginState(0)//unlogin
				//console.log("loginState after logout200:" + loginState);
			}
		})
		// .catch(function(error){
		// 	console.log("logoutGET:"+error.response.status)
		// 	console.log(error.response)
		// 	//console.log("loginState:" + loginState);
		// })
	}

  return (
    <nav class="menu">
			<div class="menu_container">
				<div class="menu_right">
					{loginState === 0?
						<Link class="link" to={'/login'}>Login</Link>
						: 
						<button class="btn btn-primary" onClick={onLogout}>log out</button> 
					}
						
				</div>
				
				<div class="menu_left">
					<Link class="link" to={'/'}>Home</Link>
				</div>
			</div>
			{/* <p>{loginState}</p> */}
    </nav>
  )
}

export default NavBar