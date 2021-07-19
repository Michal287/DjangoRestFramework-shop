import React, {Component} from "react";
import "./App.css"

import Header from "../Header";
import LandingPage from "../LandingPage";
import Footer from "../Footer";
import Login from "../user/Login";
import Register from "../user/Register"
import Cart from "../Cart"
import ProductPage from "../product/ProductPage"

import {Route, Switch, BrowserRouter as Router} from "react-router-dom";

class App extends Component {
  render() {
    return (
    <Router>
      <div className="box">

        <Header/>
          <Switch>
            <Route exact path="/" component={ LandingPage } />
            <Route path="/login" component={ Login } />
            <Route path="/register" component={ Register } />
            <Route path="/cart" component={ Cart } />
            <Route path="/product" component={ ProductPage } />

          </Switch>

        <Footer/>

      </div>

    </Router>)

  }
}

export default App