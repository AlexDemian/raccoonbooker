import React, { Component } from 'react';
import { siteUrls } from '../App.js';
import { Navbar, Nav, Form, Button } from 'react-bootstrap';

class NavbarComponent extends Component {
    
    render () {
        return (
        <Navbar bg="light" expand="lg">
        <Navbar.Brand href={ siteUrls[0].path }>Raccoon booker</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
            { siteUrls.map((url, index) =>{
                return <Nav.Link href={ url.path } key={index}>{url.label}</Nav.Link>
            })}
            </Nav>
            <Form inline>
                <Button variant="outline-success">Logout</Button>
            </Form>
        </Navbar.Collapse>
        </Navbar>)
    }
}
export default NavbarComponent;