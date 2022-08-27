import axios from "axios";

import AuthService from "./AuthService.js";

const instance = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: {
        "Content-Type": "application/json",
    },
});

instance.interceptors.request.use(
    config => {
        const access = AuthService.getAccessToken();
        if (access) {
            config.headers["Authorization"] = `Bearer ${access}`;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

instance.interceptors.response.use(
    response => {
        return response;
    },
    async error => {
        const originalConfig = error.config;
        if (!["/auth/login", "/auth/register"].includes(originalConfig.url)
            && error.response?.status === 401
            && !originalConfig._retry
        ) {
            originalConfig._retry = true;
            try {
                const refresh = AuthService.getRefreshToken();
                const response = await instance.post("/auth/token/refresh", { refresh });
                AuthService.updateAccessToken(response.data.access);
                return instance(originalConfig);
            }
            catch (_error) {
                return Promise.reject(_error);
            }
        }
        return Promise.reject(error);
    }
);

export default instance;
