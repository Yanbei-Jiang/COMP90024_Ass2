import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import HomePage from "./pages/HomePage.js";


class Router extends React.Component {
    /**url page for the project */
    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route path="/" exact component={HomePage}></Route>
                </Switch>
            </BrowserRouter>
        )
    }
}

export default Router