import React from 'react';
import { withRouter, Redirect } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Modal from 'react-bootstrap/Modal';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';

class Description extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      address: "",
      prevState: null,
      needLogin: false,
      show: false
    };
  }

  async componentDidMount() {
    const response = await fetch(`https://dry-river-74760.herokuapp.com/housings/${this.props.objectId}`).then(res => res.json());
    this.setState(response);
  }

  handleInputChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    });
  }

  handleModify(e) {
    // Store current values to this.state.prevState
    this.setState({
      prevState: this.state,
      show: true
    })
  }

  async handleSave(e) {
    const response = await fetch(`https://dry-river-74760.herokuapp.com/${this.props.objectId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.state)
    }).then(res => {
      if (res.status == 405) {
        this.setState({
          needLogin: true
        })
      } else if (res.status == 204) {
        alert('success!!!');
      } else {
        alert(`error!!!! ${res.status}`);
      }
    });
  }

  handleCancel(e) {
    // Restore the previous state
    this.state.prevState.show = false;
    this.setState(this.state.prevState);
  }

  handleClose(e) {
    this.setState({show: false});
  }

  render() {
    const {name, address, needLogin, show} = this.state;
    if (needLogin) {
      return <Redirect to='/login' />
    }
    return (
      <>
        <Modal show={show} onHide={this.handleClose.bind(this)}>
          <Modal.Header closeButton>
            <Modal.Title>Modify house information</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <InputGroup className="mb-3">
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon3">Name</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl name="name" aria-describedby="basic-addon3" value={name} onChange={this.handleInputChange.bind(this)}/>
            </InputGroup>
            <InputGroup className="mb-3">
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon3">Address</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl name="address" aria-describedby="basic-addon3" value={address} onChange={this.handleInputChange.bind(this)}/>
            </InputGroup>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="primary" onClick={this.handleSave.bind(this)}>
              Save Changes
            </Button>
            <Button variant="secondary" onClick={this.handleCancel.bind(this)}>
              Cancel
            </Button>
          </Modal.Footer>
        </Modal>

        <Container>
          <Row>
            <Col></Col>
            <Col>
              <Card style={{ width: '50em', margin: '1em' }}>
                <Card.Img variant="top" src="https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg" />
                <Card.Body>
                  <Card.Title>{name}</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">{address}</Card.Subtitle>
                  <Card.Text>
                    A property description is the written portion of a real estate listing that describes the real estate for sale or lease. Nowadays, most buyers begin their property search online. Therefore, real estate descriptions are your best chance to sway buyers and sellers.
                  </Card.Text>
                  <Button variant="primary" onClick={this.handleModify.bind(this)}>Modify</Button>
                  <Button variant="primary" style={{ margin: '1px'}}>Delete</Button>
                </Card.Body>
              </Card>
            </Col>
            <Col></Col>
          </Row>
        </Container>
      </>
    );
  }
}

function Detail(props) {
  return (
    <Description objectId={props.location.state.objectId}/>
  );
}

export default withRouter(Detail);