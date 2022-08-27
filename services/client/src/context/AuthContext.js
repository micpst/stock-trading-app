import { createContext, useContext, useEffect, useMemo, useRef, useState } from "react";

import AuthService from "../services/AuthService.js";
import decodeToken from "../utils/decodeToken.js";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);
    const timeoutId = useRef(null);

    const register = (email, firstName, lastName, password) => {
        setIsLoading(true);
        AuthService.register(email, firstName, lastName, password)
            .then(data => setIsAuthenticated(true))
            .catch(err => {
                setError(err);
                setIsAuthenticated(false);
            })
            .finally(() => setIsLoading(false));
    }

    const login = (email, password) => {
        setIsLoading(true);
        AuthService.login(email, password)
            .then(data => setIsAuthenticated(true))
            .catch(err => {
                setError(err);
                setIsAuthenticated(false);
            })
            .finally(() => setIsLoading(false));
    }

    const logout = () => {
        setIsAuthenticated(false);
        AuthService.logout();
    }

    useEffect(() => {
        AuthService.getAndVerifyRefreshToken()
            .then(token => {
                const tokenObj = decodeToken(token);
                const expireTime = (tokenObj.exp * 1000) - Date.now();
                timeoutId.current = setTimeout(() => logout(), expireTime);
                setIsAuthenticated(true);
            })
            .catch(err => {
                setError(err);
                setIsAuthenticated(false);
            })
            .finally(() => setIsLoading(false));

        return () => clearTimeout(timeoutId.current);
    }, []);

    const memoValue = useMemo(() => ({
        isAuthenticated,
        isLoading,
        error,
        login,
        logout,
        register,
    }), [isAuthenticated, isLoading, error]);

    return (
        <AuthContext.Provider
            value={memoValue}
            children={children}
        />
    );
}

export const useAuth = () => useContext(AuthContext);
