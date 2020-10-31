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
					if(response.status == 200){
						alert("Upload successfully!")
					}else{
						alert("You meet with an error!")
					}
				})
	}
	

	return(
		<div>
			<div style={{ textAlign: 'center' }}>
                <h2>  Upload a New House </h2>
      </div>

			<form onSubmit={onSubmit}>
				<label>Name</label>
				<input onChange={onNameChange}></input>

				<br/>
				<br/>

				<label>Address</label>
				<input onChange={onAddressChange}></input>

				<br/>
				<br/>

				<button onClick={onSubmit}>Submit</button>

			</form>

		</div>
	)


}

export default Upload;