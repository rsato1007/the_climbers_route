import React, { Component } from "react";
import { render } from "react-dom";
import SplashPage from "../pages/SplashPage";
import CreateRoutePage from "../pages/CreateRoutePage";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";

// When you add the routes, you'll need to do on both the Django side and the react side.
// You'll add the URL to the frontend folder URLs.
function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<SplashPage />} />
                <Route path="/create" element={<CreateRoutePage />} />
            </Routes>
        </Router>
    );
}

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);