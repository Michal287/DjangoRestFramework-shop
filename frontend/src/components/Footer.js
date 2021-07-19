import React, {Component} from 'react';
import Nav from "react-bootstrap/Nav";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFacebook, faInstagram, faLinkedin, faTwitter} from "@fortawesome/free-brands-svg-icons";

class Header extends Component {
    render() {
        return <div className="footer">
        <Nav as="ul" className="footer-nav">
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1"><b>HOME</b></Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1">CONDITIONS OF USE</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1">PRIVACY NOTICE</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1">INTEREST-BASED ADS</Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1">API</Nav.Link>
          </Nav.Item>
        </Nav>

        <Nav as="ul" className="footer-social">
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1"><b>FOLLOW US:</b></Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1"><FontAwesomeIcon icon={ faFacebook } /></Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1"><FontAwesomeIcon icon={ faInstagram } /></Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1"><FontAwesomeIcon icon={ faLinkedin } /></Nav.Link>
          </Nav.Item>
          <Nav.Item as="li">
            <Nav.Link eventKey="link-1"><FontAwesomeIcon icon={ faTwitter } /></Nav.Link>
          </Nav.Item>
        </Nav>

      </div>

    }
}

export default Header;