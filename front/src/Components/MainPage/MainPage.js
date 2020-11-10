import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import {Col, Row } from 'antd';
import { Link } from 'react-router-dom';
// import NavBar from '../NavBar/NavBar.js';
import "./MainPage.css"


function MainPage() {

    const [Houses,setHouses] = useState([])//set as array 

    
		useEffect(() => {
			Axios.get(`http://127.0.0.1:8000/housings`)
				.then(response => {
          console.log(response.data);
          console.log("housingsGET:"+response.status);
					setHouses(response.data);
				})
		},[]);
		


    const renderCards = Houses.map((house, index) => {

        return <Col lg={6} md={8} xs={24} >
                  <img style={{ width:'50%'}} src={`http://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg`} alt={"houseImage"}/>
                  <p>{house.name}</p>
                  <p>{house.address}</p>

                  {/* <Link to={'/detail/'+house._id}>Go to see detail</Link> */}
                  <Link to={{
                    pathname: '/detail',
                    state: {
                      objectId: house._id.$oid
                    }
                  }}>Go to see detail</Link>

        </Col>
    })


    return (
        <div style={{ width: '75%', margin: '3rem auto' }}>
          {/* <NavBar /> */}
            <div style={{ textAlign: 'center' }}>
                <h2>  Find Your Future Home in iHomie </h2>
            </div>

            <div>
              <Row gutter={[16, 16]}>
                {renderCards}
              </Row>
            </div>
            <br /><br />

            <div style={{ display: 'flex', justifyContent: 'center' }}>
                {/* <button onclick={() => this.props.history.push('upload')}>Upload New House</button> */}
                <Link className="link" to="/upload">Upload New House</Link>
            </div>

        </div>
    )
}

export default MainPage;