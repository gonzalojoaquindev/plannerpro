import React from 'react';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    NavLink
} from "react-router-dom";

import Inicio from './components/Inicio';
import Bla from './components/Bla';
import Parametros from './components/Parametros';
import User from './components/User';

function App() {
    return (
        <Router>
            <div className="container mt-5">
                <div className="btn-group">
                    <Link to="/" className="btn btn-dark">Inicio</Link>
                    <Link to="/bla" className="btn btn-dark">Bla bla bla</Link>
                    <NavLink to="/users" className="btn btn-dark" activeClassName="active">Users</NavLink>
                </div>
                <hr />
                <Switch>
                    <Route path="/" exact>
                        <Inicio />
                    </Route>
                    <Route path="/bla">
                        <Bla />
                    </Route>
                    <Route path="/users/:id" exact>
                        <User />
                    </Route>
                    <Route path="/users">
                        <Parametros />
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}

export default App;