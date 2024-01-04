import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';
import Login from '../pages/login';
import Cadastro from '../pages/cadastro';

const Routes = () => {
    return (
        <Switch>
            <Route path="/" element={<Login />} />
            <Route path="/cadastro" element={<Cadastro />} />
        </Switch>

    );
};

export default Routes;
