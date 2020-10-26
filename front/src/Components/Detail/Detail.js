import React from 'react';

function Preview(props) {
  return (
    <div className="preview col-md-6">
      <div className="preview-pic tab-content">
        <div className="tab-pane active" id="pic-1"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></div>
        <div className="tab-pane" id="pic-2"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></div>
        <div className="tab-pane" id="pic-3"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></div>
        <div className="tab-pane" id="pic-4"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></div>
        <div className="tab-pane" id="pic-5"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></div>
      </div>
      <ul className="preview-thumbnail nav nav-tabs">
        <li className="active"><a data-target="#pic-1" data-toggle="tab"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></a></li>
        <li><a data-target="#pic-2" data-toggle="tab"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></a></li>
        <li><a data-target="#pic-3" data-toggle="tab"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></a></li>
        <li><a data-target="#pic-4" data-toggle="tab"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></a></li>
        <li><a data-target="#pic-5" data-toggle="tab"><img src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" /></a></li>
      </ul>
    </div>
  );
}

export function Rating(props) {
  return (
    <div className="rating">
      <div className="stars">
        {props.stars >= 1 ? <span className="fa fa-star checked" /> : <span className="fa fa-star" />}
        {props.stars >= 2 ? <span className="fa fa-star checked" /> : <span className="fa fa-star" />}
        {props.stars >= 3 ? <span className="fa fa-star checked" /> : <span className="fa fa-star" />}
        {props.stars >= 4 ? <span className="fa fa-star checked" /> : <span className="fa fa-star" />}
        {props.stars >= 5 ? <span className="fa fa-star checked" /> : <span className="fa fa-star" />}
      </div>
      {typeof props.numReviews !== "undefined" && <span className="review-no">{props.numReviews} reviews</span>}
    </div>
  );
}

function DeleteButton(props) {
  function handleClick(e) {
  }

  return (
    <button className="add-to-cart btn btn-default" type="button">Delete</button>
  );
}

function ModifyButton(props) {
  function handleClick(e) {

  }

  return (
    <button className="add-to-cart btn btn-default" type="button">Modify</button>
  );
}

class Description extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "fake name",
      address: "fake address",
      viewMode: true,
      prevState: null
    };
  }

  async componentDidMount() {
    const response = await fetch("http://localhost:8000/housings/1").then(res => res.json());
    this.setState(response);
  }

  handleInputChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    });
  }

  handleButtonClick(e) {
    this.setState(prevState => {
      return {viewMode: !prevState.viewMode};
    });
  }

  handleModify(e) {
    // Store current values to this.state.prevState
    this.setState({
      prevState: this.state
    })
    this.handleButtonClick(e);
  }

  async handleSave(e) {
    const response = await fetch('http://localhost:8000/housings/1', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.state)
    }).then(res => {
      if (res.status == 204) {
        alert('success!!!');
        this.handleButtonClick(e);
      } else {
        alert('error!!!!');
      }
    });
  }

  handleCancel(e) {
    // Restore the previous state
    this.setState(this.state.prevState);
  }

  render() {
    const {name, address, viewMode} = this.state;
    return (
      <div className="details col-md-6">
        <>
          {viewMode && <h3 className="product-title">{name}</h3>}
          {viewMode && <p className="product-description">{address}</p>}
          {!viewMode && <input type="text" className="product-title" name="name" value={name} onChange={this.handleInputChange.bind(this)}/>}
          {!viewMode && <input type="text" className="product-description" name="address" value={address} onChange={this.handleInputChange.bind(this)}/>}
          <Rating stars="2" numReviews="99"/>
          <p className="product-description">A property description is the written portion of a real estate listing that describes the real estate for sale or lease. Nowadays, most buyers begin their property search online. Therefore, real estate descriptions are your best chance to sway buyers and sellers.</p>
          <h4 className="price">current price: <span>$1800</span></h4>
          <p className="vote"><strong>Property ID</strong> 15599</p>
          <p className="vote"><strong>Location</strong> US</p>
          <p className="vote"><strong>Property Type</strong> House</p>
          <p className="vote"><strong>Status</strong> Rent</p>
  
          <div className="action">
            <>
              {viewMode && <button className="add-to-cart btn btn-default" type="button" onClick={this.handleModify.bind(this)}>Modify</button>}
              {viewMode && <button className="add-to-cart btn btn-default" type="button" onClick={this.handleButtonClick.bind(this)}>Delete</button>}
              {!viewMode && <button className="add-to-cart btn btn-default" type="button" onClick={this.handleSave.bind(this)}>Save</button>}
              {!viewMode && <button className="add-to-cart btn btn-default" type="button" onClick={this.handleCancel.bind(this)}>Cancel</button>}
            </>
          </div>
        </>
      </div>
    );
  }
}

/*
async function Description(props) {
  const response = await fetch("/housings/1").then(res => res.json());
  props.name = response.name;
  props.address = response.address;
  console.log(response);
  return (
    <div className="details col-md-6">
      <>
        <h3 className="product-title">{props.name}</h3>
        <p className="product-description">{props.address}</p>
        <Rating stars="2" numReviews="99"/>
        <p className="product-description">A property description is the written portion of a real estate listing that describes the real estate for sale or lease. Nowadays, most buyers begin their property search online. Therefore, real estate descriptions are your best chance to sway buyers and sellers.</p>
        <h4 className="price">current price: <span>$1800</span></h4>
        <p className="vote"><strong>Property ID</strong> 15599</p>
        <p className="vote"><strong>Location</strong> US</p>
        <p className="vote"><strong>Property Type</strong> House</p>
        <p className="vote"><strong>Status</strong> Rent</p>

        <div className="action">
          <>
            <DeleteButton />
            <ModifyButton />
          </>
        </div>
      </>
    </div>
  );
}
*/

function Container(props) {
  return (
    <>
    <div className="container">
      <div className="card">
        <div className="container-fliud">
          <div className="wrapper row">
            <>
              <Preview />
              <Description />
            </>
          </div>
        </div>
      </div>
    </div>
    </>
  );
}

function Detail(props) {
  return (
    <Container />
  );
}

export default Detail;