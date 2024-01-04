import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';
import Login from '../pages/login';
import Cadastro from '../pages/cadastro';
import AdmPage from '../pages/adm-page';

const Routes = () => {
    return (
        <Switch>
            <Route path="/" element={<Login />} />
            <Route path="/cadastro" element={<Cadastro />} />
            <Route path='/admin' element={<AdmPage />} />
        </Switch>

    );
};

export default Routes;
