import React from "react";
import { CircularProgress, Stack } from "@mui/material";

const LoadingScreen = () => (
    <Stack
        height="100vh"
        alignItems="center"
        justifyContent="center"
    >
        <CircularProgress
            size={80}
            thickness={2}
            disableShrink
        />
    </Stack>
);

export default LoadingScreen;
