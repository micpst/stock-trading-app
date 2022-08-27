import React from "react";
import { Navigate, Outlet } from "react-router-dom";

import LoadingScreen from "./LoadingScreen.jsx";
import { useAuth } from "../context/AuthContext.js";

const PrivateRoute = () => {
    const { isAuthenticated, isLoading } = useAuth();
    if (isLoading) {
        return <LoadingScreen />;
    }
    return isAuthenticated ? <Outlet /> : <Navigate to="login" />;
}

export default PrivateRoute;
