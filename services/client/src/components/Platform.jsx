import React , { Fragment } from "react";
import { Outlet } from "react-router-dom";

const Platform = () => (
    <Fragment>
        platform
        <Outlet />
    </Fragment>
);

export default Platform;
