import React, {Component} from 'react';
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faShoppingCart, faUserLock} from "@fortawesome/free-solid-svg-icons";
import { MDBDropdown, MDBDropdownToggle, MDBDropdownMenu, MDBDropdownItem } from "mdbreact";


class Header extends Component {
    render() {
        return <Navbar>

          <Navbar.Brand href="#home">TechShop</Navbar.Brand>

          <Nav className="mr-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Support</Nav.Link>
          </Nav>

          <Form inline>
            <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          </Form>

          <Nav className="lp-utility">
            <Nav.Link><FontAwesomeIcon icon={ faShoppingCart } /></Nav.Link>
            <Nav><MDBDropdown>
              <MDBDropdownToggle caret color="primary">
                <FontAwesomeIcon icon={ faUserLock } />
              </MDBDropdownToggle>
              <MDBDropdownMenu basic>
                <MDBDropdownItem>Regular link</MDBDropdownItem>
                <MDBDropdownItem disabled href="#">
                  Disabled link
                </MDBDropdownItem>
                <MDBDropdownItem href="#">Another link</MDBDropdownItem>
              </MDBDropdownMenu>
            </MDBDropdown></Nav>
          </Nav>

        </Navbar>

    }
}

export default Header;