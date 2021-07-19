import React, {Component} from 'react';
import ProductFilter from "./product/ProductFilter";
import ProductList from "./product/ProductList";

class ProductPage extends Component {
    render() {
        return<div className="box">
            <ProductFilter/>
            <ProductList/>
        </div>


    }
}

export default ProductPage;