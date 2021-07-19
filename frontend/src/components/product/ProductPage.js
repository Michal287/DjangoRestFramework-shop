import React, {Component} from 'react';
import {
    MDBCard,
    MDBCardBody,
    MDBCardFooter,
    MDBCardText,
    MDBCardTitle,
    MDBView,
    MDBMask,
    MDBTooltip
} from "mdbreact";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faShoppingCart} from "@fortawesome/free-solid-svg-icons";
import Nav from "react-bootstrap/Nav";

class ProductPage extends Component {
    render() {
        return <div className="detail-page">

            <MDBView hover rounded className="card-image z-depth-1-half mb-4">
              <img
                className="img-fluid"
                src="https://mdbootstrap.com/img/Photos/Others/images/86.jpg"
                alt=""
              />
              <a href="#!">
                <MDBMask overlay="white-slight" className="waves-light" />
              </a>
            </MDBView>



            <MDBCard className="cart-details">

                <div className="cart-text-box">

                        <MDBCardBody cascade className='text-center'>
                          <MDBCardTitle>
                            <strong>
                              <a href='#!'>GoPro</a>
                            </strong>
                              <a href='#!' className='text-muted'>
                                <h5>Camera</h5>
                              </a>
                            <MDBCardText>Lorem ipsum dolor sit amet, consectetur adipisicing minima veniam elit. Lorem ipsum dolor sit amet, consectetur adipisicing minima veniam elit.Lorem ipsum dolor sit amet, consectetur adipisicing minima veniam elit.</MDBCardText>
                          </MDBCardTitle>

                          <MDBCardFooter className='px-1'>
                            <span className='float-right font-weight-bold'>
                              <strong>1439$</strong>
                            </span>
                            <span className='float-left'>
                              <MDBTooltip domElement placement='top' className="cart-icon">
                                <Nav.Link><FontAwesomeIcon icon={ faShoppingCart } /></Nav.Link>
                                <span>Remove item</span>
                              </MDBTooltip>
                              <MDBTooltip domElement placement='top'>
                                <i className='grey-text fa fa-heart' />
                                <span>Add to Whishlist</span>
                              </MDBTooltip>
                            </span>
                          </MDBCardFooter>

                        </MDBCardBody>

                  </div>

            </MDBCard>


        </div>

    }
}

export default ProductPage;