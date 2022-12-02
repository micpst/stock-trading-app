import React, { useState } from "react";
import { Box, Button, Container, TextField } from "@mui/material";

import { useAuth } from "../context/AuthContext.js";

const LogIn = () => {
    const { login } = useAuth();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleEmailChange = e => {
        setEmail(e.target.value);
    }

    const handlePasswordChange = e => {
        setPassword(e.target.value);
    }

    const handleFormSubmit = e => {
        e.preventDefault();
        login(email, password);
    }

    return (
        <Container component="main" maxWidth="xs">
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Box
                    component="form"
                    onSubmit={handleFormSubmit}
                    noValidate
                    sx={{mt: 1}}
                >
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email Address"
                        name="email"
                        autoComplete="email"
                        autoFocus
                        value={email}
                        onChange={handleEmailChange}
                    />
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        autoComplete="current-password"
                        value={password}
                        onChange={handlePasswordChange}
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{mt: 3, mb: 2}}
                    >
                        Login
                    </Button>
                    <Button
                        type="submit"
                        fullWidth
                        variant="outlined"
                        sx={{mt: 3, mb: 2}}
                    >
                        Create new account
                    </Button>
                </Box>
            </Box>
        </Container>
    );
}

export default LogIn;
