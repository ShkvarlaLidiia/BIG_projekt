import { Header } from "./components/Header/Header";
import { Navigation } from "./components/Navigation/Navigation";
import { Main } from "./components/Main/Main";
import { Footer } from "./components/Footer/Footer";

import { render } from "./core/render";
import { getData } from "./utils/getData";

import "./public/styles/style.css";
import { Component } from "./core/Component";

// let isLoading = true;
// const products = [];
const header = new Header({
    tagName : "header",
    className : "header",
    children : '<h2>Logo</h2>',
    }).toHTML();

// const data = getData("http://127.0.0.1:3333/products", products);

const nav = new Navigation({
    tagName : "nav",
    className : "nav",
    children : '<h3>Navigation</h3>',
    }).toHTML();

const main = new Main({
    tagName : "main",
    className : "main",
    children : '<h1>Main</h1>',

    // children: isLoading ? "..." : products,
    // children : '<h2>Products</h2>',
    // events : (e) => getData("http://127.0.0.1:5000/products"),
    }).toHTML();
    
const footer = new Footer({
    tagName : "footer",
    className : "footer",
    children : '<h2>Footer</h2>',

    }).toHTML();
    
render("#app", [header, main, footer]);
render("header", nav)
