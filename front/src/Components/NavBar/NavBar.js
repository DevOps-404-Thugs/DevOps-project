import React, { useState, useEffect } from 'react';
// import { Link } from 'react-router-dom';
import Axios from 'axios'
import "./NavBar.css"
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

export function NavBar() {
	const [loginState, setLoginState] = useState(false); //default as unlogin

	useEffect(() => {
		Axios.get(`/login`,{withCredentials: true})
		.then(response => {
			console.log("loginGET:"+response.status)
			console.log(response)
			if(response.status === 200){
				setLoginState(true);
			}else if(response.status === 205){
				setLoginState(false); // unlogin
			}
		})
		.catch(function(error){
			console.log("loginGET:"+error.response.status)
			console.log(error.response)
			
		})

		
	},[]);
	console.log(loginState);

	const onLogout = (event) => {
		Axios.get(`/logout`, {withCredentials: true})
		.then(response => {
			console.log("logoutGET:"+response.status)
			console.log(response)
			if(response.status === 200){
				setLoginState(false); // unlogin
			}
		})
		.catch(function(error){
			console.log("logoutGET:"+error.response.status)
			console.log(error.response)
		})
	}

	const onLogin = (event) => {
		window.location = "/ihomie#/login";
	}

  return (
	  <Navbar bg="light" expand="lg">
		  <Navbar.Brand href="/ihomie">iHomie</Navbar.Brand>
		  <Navbar.Toggle aria-controls="basic-navbar-nav" />
		  <Navbar.Collapse id="basic-navbar-nav">
			<Nav className="mr-auto">
			  <Nav.Link href="/ihomie">Home</Nav.Link>
			  <Nav.Link href="/ihomie#/upload">Upload</Nav.Link>
			  <Nav.Link href="/ihomie#/register">Register</Nav.Link>
			  <Nav.Link href="/ihomie#/account">Account</Nav.Link>
			</Nav>
			<Form inline>
			  {loginState === false?
				  <Button variant="outline-primary" onClick={onLogin}>Login</Button>
				  :
				  <Button variant="primary" onClick={onLogout}>Logout</Button>
			  }
			</Form>
		  </Navbar.Collapse>
		</Navbar>
	)
  
}

export default NavBar