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

// const data = getData("http://127.0.0.1:5000/products", products);

const nav = new Navigation({
    tagName : "nav",
    className : "nav",
    children : '<ul><li><a href="#">Catalogs</a></li><li><a href="#">Contacts</a></li><li><a href="#">Login</a></li></ul>'
    }).toHTML();

    //  '<h3>Navigation</h3>',


const main = new Main({
    tagName : "main",
    className : "main",
    children : '<button id="get-data">Get data</button><div id="trecks"></div>',

    // '<h2>Main</h2>'
    // '<div id="trecks"></div><button id="get-data">Get data</button>',    

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




const btn = document.getElementById("get-data");
const trecks = document.getElementById("trecks");


btn.addEventListener("click", (e) => {
    e.preventDefault();

    (async function () {
        const data = await fetch("http://127.0.0.1:5000/");
        const parsedData = await data.json();
        // await console.log(parsedData);
        const domArr = await parsedData.map((el) => {
            return `
                <h2>
                    author : ${el.author}
                </h2>
                <h2>
                    name : ${el.name}
                </h2>
                <h2>
                    year : ${el.year}
                </h2>
            `;
        });
        
        trecks.insertAdjacentHTML("afterbegin", domArr);
    })();
});   

