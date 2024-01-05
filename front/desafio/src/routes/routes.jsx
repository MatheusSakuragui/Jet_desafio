import React from 'react';
import { Route, Routes as Switch } from 'react-router-dom';
import Login from '../pages/login';
import Cadastro from '../pages/cadastro';
import AdmPage from '../pages/adm-page';
import Home from '../pages/home';
import Leilao from '../pages/leilao';

const Routes = () => {
    return (
        <Switch>
            <Route path="/" element={<Login />} />
            <Route path="/cadastro" element={<Cadastro />} />
            <Route path='/leilao/:id' element={<Leilao/>} /> 
            <Route path='/admin' element={<AdmPage />} />
            <Route path='/home' element={<Home />} />
        </Switch>

    );
};

export default Routes;