import React, {Component} from 'react';
import {
  MDBCard,
  MDBCardBody,
  MDBIcon,
  MDBCardHeader,
  MDBBtn,
  MDBInput
} from "mdbreact";

import { MDBContainer, MDBRow, MDBCol } from 'mdbreact';

class Register extends Component {
    render() {
        return (
        <div className="login">


                  <MDBCard>
                    <MDBCardBody>
                      <MDBCardHeader className="form-header deep-blue-gradient rounded">
                        <h3 className="my-1 pl-5">
                          <MDBIcon icon="lock" /> Sign up
                        </h3>
                      </MDBCardHeader>
                      <MDBContainer>
                          <MDBRow>
                            <MDBCol md="12">
                              <form>
                                <div className="grey-text">
                                  <MDBInput label="Your name" icon="user" group type="text" validate error="wrong"
                                    success="right" />
                                  <MDBInput label="Your email" icon="envelope" group type="email" validate error="wrong"
                                    success="right" />
                                  <MDBInput label="Confirm your email" icon="exclamation-triangle" group type="text" validate
                                    error="wrong" success="right" />
                                  <MDBInput label="Your password" icon="lock" group type="password" validate />
                                </div>
                                <div className="text-center">
                                  <MDBBtn color="primary">Register</MDBBtn>
                                </div>
                              </form>
                            </MDBCol>
                          </MDBRow>
                      </MDBContainer>
                    </MDBCardBody>
                  </MDBCard>

        </div>
          );

    }
}

export default Register;