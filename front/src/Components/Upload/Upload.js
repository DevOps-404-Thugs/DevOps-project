import React, { useState } from 'react'
import Axios from 'axios'

function Upload() {
	const [nameValue, setNameValue] = useState("")
	const [addressValue, setAddressValue] = useState("") 

	const onNameChange = (event) => {
		setNameValue(event.currentTarget.value)
	}

	const onAddressChange = (event) => {
		setAddressValue(event.currentTarget.value)
	}

	const onSubmit = (event)=>{
		event.preventDefault();
		if(!nameValue || !addressValue){
			return alert("Please fill in all fields!")
		}
		console.log(nameValue)
		console.log(addressValue)
		const variables = {
			name : nameValue,
			address : addressValue
		}
		
		Axios.post(`http://127.0.0.1:8000/housings`, variables)
					.then(response => {
						console.log(response.status)
						console.log(response)
						if(response.status === 200){
							alert("Upload successfully!")
						}else{
							alert("You meet with an error!")
						}
					})
					.catch(function(error){
						console.log(error.response)
						if(error.status === 400){
							alert("Parameter wrong!")
						}
					})
	}
	

	return(
		<div>
			<div style={{ width: '75%', margin: '3rem auto' }}>
        <form>
					<div class="form-group">
						<label>House Name</label>
						<input type="text" onChange={onNameChange} class="form-control" id="email-input" placeholder="Input your email address here"></input>
					</div>
					<div class="form-group">
						<label>Address</label>
						<input type="text" onChange={onAddressChange} class="form-control" id="password-input" placeholder="Input your password here"></input>
					</div>

					<button type="submit" class="btn btn-primary" onClick={onSubmit} >Submit</button>
        </form>
			</div>
		</div>
	)


}

export default Upload;