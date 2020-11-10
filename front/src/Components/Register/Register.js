import React, { useState } from 'react'
import Axios from 'axios'
import { Link } from 'react-router-dom';


function Register() {
		const [usernameValue, setUsernameValue] = useState("") 
		const [emailValue, setEmailValue] = useState("") 
		const [passwordValue, setPasswordValue] = useState("") 

		const onUsernameChange = (event) => {
			setUsernameValue(event.currentTarget.value)
		}

		const onEmailChange = (event) => {
			setEmailValue(event.currentTarget.value)
		}

		const onPasswordChange = (event) => {
			setPasswordValue(event.currentTarget.value)
		}

	
		const onSubmit = (event) =>{
			event.preventDefault();
			if(!usernameValue || !emailValue || !passwordValue){
				return alert("Please fill in all fields!")
			}
			console.log(usernameValue)
			console.log(emailValue)
			console.log(passwordValue)

			const variables = {
				username : usernameValue,
				email : emailValue,
				password : passwordValue
			}
			
			console.log(variables)

			Axios.post(`https://dry-river-74760.herokuapp.com/register`, variables)
					.then(response => {
						console.log(response.status)
						console.log(response)
						if(response.status === 200){
							alert("Register successfully!")
						}else{
							alert("You meet with an error!")
						}
					})
					.catch(function(error){
						console.log(error.response)
						if(error.response.status === 401){
							alert("The email has been registered!")
						}else if(error.response.status === 402){
							alert("This username is unavailable!")
						}else if(error.response.status === 400){
							alert("You have loged in already!")
						}
						else if(error.response.status === 403){
							alert("Parameter wrong!")
						}
					})
		}

    return (
      <div style={{ width: '75%', margin: '3rem auto' }}>
        <form>
				<div class="form-group">
						<label>Username</label>
						<input type="text" onChange={onUsernameChange} class="form-control" id="email-input" placeholder="Input username here"></input>
					</div>
					<div class="form-group">
						<label>Email address</label>
						<input type="email" onChange={onEmailChange} class="form-control" id="email-input" placeholder="Input your email address here"></input>
					</div>
					<div class="form-group">
						<label>Password</label>
						<input type="password" onChange={onPasswordChange} class="form-control" id="password-input" placeholder="Input your password here"></input>
					</div>

					<button type="submit" class="btn btn-primary" onClick={onSubmit}>Submit</button>
        </form>
			
        <small class="text-muted">
				Already Have An Account? <Link className="link" to="/login">Sign In</Link>
			</small>
            

      </div>
    )
}

export default Register;