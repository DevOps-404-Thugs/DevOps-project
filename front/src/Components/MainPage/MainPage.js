import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import { Icon, Col, Card, Row } from 'antd';

const { Meta } = Card;

function MainPage() {

    const [Houses,setHouses] = useState([])//set as array 

    
		useEffect(() => {
			Axios.get(`http://127.0.0.1:8000/housings`)
				.then(response => {
					console.log(response.data);
					setHouses(response.data);
				})
		},[]);
		


    const renderCards = Houses.map((house, index) => {

        return <Col lg={6} md={8} xs={24} >
            <Card
                hoverable={true}
                cover={<img style={{ width:'50%'}} src={`https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg`} alt="houseImage"/>}
            >
              <Meta
                    title={house.name}
                    description={house.address}
              />
            </Card>
        </Col>
    })

    return (
        <div style={{ width: '75%', margin: '3rem auto' }}>
            <div style={{ textAlign: 'center' }}>
                <h2>  Find Your Future Home in iHomie </h2>
            </div>

            <div>
              <Row gutter={[16, 16]}>
                {renderCards}
              </Row>
            </div>
            <br /><br />


        </div>
    )
}

export default MainPage
