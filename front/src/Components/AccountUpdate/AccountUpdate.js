import React, { useState } from 'react'
import Axios from 'axios'

function Upload() {
	const [usernameValue, setUsernameValue] = useState("")
	const [emailValue, setEmailValue] = useState("") 

	const onUsernameChange = (event) => {
		setUsernameValue(event.currentTarget.value)
	}

	const onEmailChange = (event) => {
		setEmailValue(event.currentTarget.value)
	}

	const onSubmit = (event)=>{
		event.preventDefault();
		if(!usernameValue || !emailValue){
			return alert("Please fill in all fields!")
		}
		console.log(usernameValue)
		console.log(emailValue)
		const variables = {
			username : usernameValue,
			email : emailValue
		}
		
		Axios.put(`/account`, variables, {withCredentials: true})
					.then(response => {
						console.log(response.status)
						console.log(response)
						if(response.status === 200){
                            alert("Account updated successfully!")
                            window.location.replace('/ihomie')//automatically jump to mainpage
						}else{
							alert("You meet with an error!")
						}
                    })
                    .catch(function(error){
                        console.log(error.response)
                        if(error.response.status === 400){
							alert("This account has existed!")
						}
					})
	}
	

	return(
		<div>
			<div style={{ width: '75%', margin: '3rem auto' }}>
        <form>
					<div class="form-group">
						<label>User Name</label>
						<input type="text" onChange={onUsernameChange} class="form-control" id="username-input" placeholder="Input new username here"></input>
					</div>
					<div class="form-group">
						<label>Email</label>
						<input type="text" onChange={onEmailChange} class="form-control" id="email-input" placeholder="Input new email address here"></input>
					</div>

					<button type="submit" class="btn btn-primary" onClick={onSubmit} >Submit</button>
        </form>
			</div>
		</div>
	)


}

export default Upload;