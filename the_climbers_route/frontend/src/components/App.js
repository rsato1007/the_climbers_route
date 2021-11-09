import React, { Component } from "react";
import { render } from "react-dom";
import NavBar from "../components/NavBar/index";
import { BrowserRouter as Router } from "react-router-dom";

// When you add the routes, you'll need to do on both the Django side and the react side.
// You'll add the URL to the frontend folder URLs.
function App() {
    return (
        <Router>
            <NavBar />
        </Router>
    );
}

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);