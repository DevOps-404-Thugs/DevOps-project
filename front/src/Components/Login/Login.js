import React, { useState, useEffect } from 'react'
import Axios from 'axios'
import { Link } from 'react-router-dom';



function Login() {
		const [emailValue, setEmailValue] = useState("") 
		const [passwordValue, setPasswordValue] = useState("") 

		const onEmailChange = (event) => {
			setEmailValue(event.currentTarget.value)
		}

		const onPasswordChange = (event) => {
			setPasswordValue(event.currentTarget.value)
		}

	
		const onSubmit = (event) =>{
			event.preventDefault();
			if(!emailValue || !passwordValue){
				return alert("Please fill in all fields!")
			}

			console.log(emailValue)
			console.log(passwordValue)

			const variables = {
				email : emailValue,
				password : passwordValue
			}
			
			console.log(variables)

			Axios.post(`/login`, variables, {withCredentials: true})
					.then(response => {
						console.log(response.status)
						console.log(response)
						if(response.status === 200){
							alert("Login successfully!")
							window.location.replace('/ihomie')//automatically jump to mainpage
						}else{
							alert("You meet with an error!")
						}
					})
					.catch(function(error){
						console.log(error.response)
						if(error.response.status === 401){
							alert("You need to register for the account!")
						}else if(error.response.status === 400){
							alert("Password Error!")
						}else if(error.response.status === 402){
							alert("Parameters Error!")
						}
					})
		}

		// const onTest = (event) =>{

		// 	Axios.get(`http://127.0.0.1:8000/login`,  {withCredentials: true})
		// 			.then(response => {
		// 				console.log(response.status)
		// 				console.log(response)
						
		// 			})
		// 			.catch(function(error){
		// 				console.log(error.response)
						
		// 			})
		// }
		

    return (
      <div style={{ width: '75%', margin: '3rem auto' }}>
        <form>
					<div class="form-group">
						<label>Email address</label>
						<input type="email" onChange={onEmailChange} class="form-control" id="email-input" placeholder="Input your email address here"></input>
					</div>
					<div class="form-group">
						<label>Password</label>
						<input type="password" onChange={onPasswordChange} class="form-control" id="password-input" placeholder="Input your password here"></input>
					</div>

					<button type="submit" class="btn btn-primary" onClick={onSubmit} >Submit</button>
        </form>
			
			<small class="text-muted">
				Need An Account? <Link className="link" to="/register">Sign Up Now</Link>
			</small>
            
			{/* <button class="btn btn-primary"  onClick={onTest}>test</button>  */}
      </div>
    )
}

export default Login;