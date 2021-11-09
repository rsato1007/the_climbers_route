import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import SplashPage from "../../pages/SplashPage";
import CreateRoutePage from "../../pages/CreateRoutePage";

const NavBar = () => {
    return (
        <div>
            <div className="nav_bar">
                Insert Routes.
            </div>
            <Routes>
                <Route path="/" element={<SplashPage />} />
                <Route path="route/new" element={<CreateRoutePage />} />
            </Routes>
        </div>
    )
}

export default NavBar;