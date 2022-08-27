import api from "./api.js";

const register = (email, firstName, lastName, password) => {
    return api
        .post("/auth/register", {
            email: email,
            first_name: firstName,
            last_name: lastName,
            password: password
        })
        .then(response => {
            setTokens(response.data);
            return response.data;
        });
}

const login = (email, password) => {
    return api
        .post("/auth/login", { email, password })
        .then(response => {
            setTokens(response.data);
            return response.data;
        });
}

const logout = () => {
    localStorage.removeItem("tokens");
}

const getAndVerifyRefreshToken = () => {
    const token = getRefreshToken();
    return api.post("/auth/token/verify", { token })
        .then(response => token);
}

const getRefreshToken = () => {
    const tokens = JSON.parse(localStorage.getItem("tokens"));
    return tokens?.refresh;
}

const getAccessToken = () => {
    const tokens = JSON.parse(localStorage.getItem("tokens"));
    return tokens?.access;
}

const setTokens = tokens => {
    localStorage.setItem("tokens", JSON.stringify(tokens));
}

const updateAccessToken = token => {
    let tokens = JSON.parse(localStorage.getItem("tokens"));
    tokens.access = token;
    localStorage.setItem("tokens", JSON.stringify(tokens));
}

const AuthService = {
    register,
    login,
    logout,
    getAccessToken,
    getRefreshToken,
    updateAccessToken,
    getAndVerifyRefreshToken,
};

export default AuthService;
