import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Typography, Card, CardContent, Grid } from '@mui/material';
import NavBar from '../components/navBar';

export default function Leilao() {
    const { id } = useParams();
    const [leilao, setLeilao] = useState(null);

    useEffect(() => {
        const fetchLeilao = async () => {
            try {
                const response = await axios.get(`http://localhost:5000/leilao/${id}`);
                setLeilao(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchLeilao();
    }, [id]);

    if (!leilao) {
        return <div>Carregando...</div>;
    }

    return (
        <>
            <NavBar/>
        <Grid container spacing={3} justifyContent="center">
            <Grid item xs={12} md={6}>
                <Card>
                    <CardContent>
                        <Typography variant="h4" gutterBottom>
                            {leilao.nome}
                        </Typography>
                        <Typography variant="subtitle1" color="textSecondary" gutterBottom>
                            ID: {leilao.id}
                        </Typography>
                        <Typography variant="subtitle1" color="textSecondary">
                            <b>Início:</b> {leilao.data_futura}
                        </Typography>
                        <Typography variant="subtitle1" color="textSecondary">
                            <b>Fim:</b> {leilao.data_visitacao}
                        </Typography>

                        <Typography variant="h6" color="primary" paragraph>
                            Detalhes:
                        </Typography>
                        <Typography variant="body1">
                            {leilao.detalhes}
                        </Typography>

                        <Typography variant="h6" color="primary" paragraph>
                            Produtos:
                        </Typography>
                        {leilao.produtos.map((produto) => (
                            <div key={produto.id}>
                                <Typography variant="subtitle1" color="textSecondary">
                                    <b>Marca:</b> {produto.marca}
                                </Typography>
                                <Typography variant="subtitle1" color="textSecondary">
                                    <b>Modelo:</b> {produto.modelo}
                                </Typography>
                                <Typography variant="subtitle1" color="textSecondary">
                                    <b>Descrição:</b> {produto.descricao}
                                </Typography>
                                <Typography variant="subtitle1" color="textSecondary">
                                    <b>Lance Inicial:</b> {produto.lance_inicial}
                                </Typography>
                                <Typography variant="subtitle1" color="textSecondary">
                                    <b>Lance Adicional:</b> {produto.lance_adicional}
                                </Typography>
                                <Typography variant="subtitle1" color="textSecondary">
                                    <b>Vendido:</b> {produto.vendido ? 'Sim' : 'Não'}
                                </Typography>
                            </div>
                        ))}
                    </CardContent>
                </Card>
            </Grid>
        </Grid>
                        </>
    );
}
