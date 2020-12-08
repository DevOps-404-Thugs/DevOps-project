import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import { Link } from 'react-router-dom';
import Card from 'react-bootstrap/Card';


function Account() {

    const [user,setUser] = useState({username:null, password:null})

    useEffect(() => {
        Axios.get(`/account`)
            .then(response => {
                console.log(response.data);
                setUser(response.data);
            })
            .catch(function(error){
                console.log(error.response)
                
            })
        
        console.log(user);    
    });
		

    return (
        <div style={{ width: '50%', margin: '3rem auto'}}>
            {user.username == null?
                <h2 style={{ display: 'flex', justifyContent: 'center' }}>You need to login first!</h2>
                :
                <div>
                    <Card style={{ 'margin-bottom': '30px' }}>
                        <Card.Header style={{ textAlign: 'center' }}>Account Info</Card.Header>
                        <Card.Title style={{ 'padding-top': '0.75rem','padding-left': '1rem'}}>username: {user.username}</Card.Title>
                        <Card.Text style={{ 'padding-bottom': '0.75rem','padding-left': '1rem', 'font-weight':'bold'}}>email: {user.email}</Card.Text>
                    </Card>
                    <Link className="link" to="/account_update" style={{color:'blue',display: 'flex', justifyContent: 'center'}}>Update Account Information</Link>
                </div>
			}
            

            <br /><br />


            <div style={{ display: 'flex', justifyContent: 'center' }}>
                
            </div>

        </div>
    )
}

export default Account;