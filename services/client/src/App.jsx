import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";

import LogIn from "./components/LogIn.jsx";
import SignUp from "./components/SignUp.jsx";
import Market from "./components/Market.jsx";
import History from "./components/History.jsx";
import Platform from "./components/Platform.jsx";
import PendingOrders from "./components/PendingOrders.jsx";
import OpenPositions from "./components/OpenPositions.jsx";
import PrivateRoute from "./components/PrivateRoute.jsx";
import PublicRoute from "./components/PublicRoute.jsx";

const App = () => (
    <Routes>
        <Route element={<PrivateRoute />}>
            <Route element={<Platform />}>
                <Route path="market" element={<Market />} />
                <Route path="pending-orders" element={<PendingOrders />} />
                <Route path="open-positions" element={<OpenPositions />} />
                <Route path="history" element={<History />} />
                <Route path="*" element={<Navigate to="market" />} />
            </Route>
        </Route>
        <Route element={<PublicRoute />}>
            <Route path="login" element={<LogIn />} />
            <Route path="signup" element={<SignUp />} />
            <Route path="*" element={<Navigate to="login" />} />
        </Route>
    </Routes>
);

export default App;
