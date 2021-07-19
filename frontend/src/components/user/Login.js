import React, {Component} from 'react';

import {
  MDBCard,
  MDBCardBody,
  MDBModalFooter,
  MDBIcon,
  MDBCardHeader,
  MDBBtn,
  MDBInput
} from "mdbreact";

class Login extends Component {
    render() {
        return (
        <div className="login">


                  <MDBCard>
                    <MDBCardBody>
                      <MDBCardHeader className="form-header deep-blue-gradient rounded">
                        <h3 className="my-1 pl-5">
                          <MDBIcon icon="lock" /> Sign in
                        </h3>
                      </MDBCardHeader>
                      <form>
                        <div className="grey-text">
                          <MDBInput
                            label="Type your email"
                            icon="envelope"
                            group
                            type="email"
                            validate
                            error="wrong"
                            success="right"
                          />
                          <MDBInput
                            label="Type your password"
                            icon="lock"
                            group
                            type="password"
                            validate
                          />
                        </div>

                      <div className="text-center mt-4">
                        <MDBBtn
                          color="light-blue"
                          className="mb-3"
                          type="submit"
                        >
                          Login
                        </MDBBtn>
                      </div>
                      </form>
                      <MDBModalFooter>
                        <div className="font-weight-light">
                          <p>Not a member? Sign Up</p>
                          <p>Forgot Password?</p>
                        </div>
                      </MDBModalFooter>
                    </MDBCardBody>
                  </MDBCard>

        </div>
          );

    }
}

export default Login;