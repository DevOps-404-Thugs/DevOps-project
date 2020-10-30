import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import { Link } from 'react-router-dom';
import {Button} from 'reactstrap'


function Login() {


    return (
      <div style={{ width: '75%', margin: '3rem auto' }}>
        <form>
					<div class="form-group">
						<label for="email-input">Email address</label>
						<input type="email" class="form-control" id="email-input" placeholder="Input your email address here"></input>
					</div>
					<div class="form-group">
						<label for="password-input">Password</label>
						<input type="password" class="form-control" id="password-input" placeholder="Input your password here"></input>
					</div>

					<button type="submit" class="btn btn-default">Submit</button>
        </form>
			
			<small class="text-muted">
				Need An Account? <Link className="link" to="/register">Sign Up Now</Link>
			</small>
            

      </div>
    )
}

export default Login;