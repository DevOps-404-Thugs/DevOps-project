import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import {Col, Row } from 'antd';
import { Link } from 'react-router-dom';
// import NavBar from '../NavBar/NavBar.js';


function MainPage() {

    const [Houses,setHouses] = useState([])//set as array 
    // const [picture, setPicture] = useState()//picture url

    
		useEffect(() => {
			Axios.get(`/housings`)
				.then(response => {
          console.log(response.data);
          console.log("housingsGET:"+response.status);
          setHouses(response.data);
          console.log(Houses)
				})
		},[]);
		


    const renderCards = Houses.map((house, index) => {
      // Axios.get(`https://api.unsplash.com/photos/random?query=house&client_id=1vH0e4mIPBBiGM37PkUm8BDCDOXYgqEmGeGgbfFxXG8`)
      // .then(response => {
      //   console.log("========================")
      //   console.log(response.data);
      //   console.log(response.data.urls.small);
      //   setPicture(response.data.urls.small)
      // })
      

        return <Col lg={6} md={8} xs={24} style={{ border: '#CCC solid 1px', 'border-radius' : '10px', padding:'30px', margin:'30px auto 30px'}}>
                  <img style={{ width: '100%'}} src={`https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg`} alt={"houseImage"}/>
                  {/* <img style={{ width: '100%', height:'300px'}} src={picture} alt={"houseImage"}/> */}
                  <p style={{ 'padding-top':'10px', margin : '0', 'font-size' : '24px', 'font-weight' : '700'}}>{house.name}</p>
                  <p style={{ 'padding-top':'10px', 'padding-bottom':'5px', margin : '0'}}>{house.address}</p>

                  {/* <Link to={'/detail/'+house._id}>Go to see detail</Link> */}
                  <Link style={{ 'padding-top':'10px', margin : '0'}} to={{
                    pathname: '/detail',
                    state: {
                      objectId: house._id.$oid
                    }
                  }}>Go to see detail</Link>

        </Col>
    })


    return (
        <div style={{ width: '65%', margin: '3rem auto' }}>
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

            <div style={{ display: 'flex', justifyContent: 'center'}}>
                {/* <button onclick={() => this.props.history.push('upload')}>Upload New House</button> */}
                <Link className="link" to="/upload">Upload New House</Link>
            </div>

            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Link className="link" to="/account_update" style={{color:'orange'}}>Update Account Information</Link>
            </div>

        </div>
    )
}

export default MainPage;