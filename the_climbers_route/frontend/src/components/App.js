import React, { Component } from "react";
import { render } from 'react-dom';

// When you add the routes, you'll need to do on both the Django side and the react side.
// You'll add the URL to the frontend folder URLs.
function App() {
    return (
        <div>
            This is the React sanity check
        </div>
    )
}

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);