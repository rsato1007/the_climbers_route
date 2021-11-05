import React, { Component } from "react";
import { render } from 'react-dom';

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