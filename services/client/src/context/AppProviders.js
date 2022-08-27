import React from "react";

import { AuthProvider } from "./AuthContext.js";

const AppProviders = ({ children }) => (
    <AuthProvider>
        {children}
    </AuthProvider>
);

export default AppProviders;