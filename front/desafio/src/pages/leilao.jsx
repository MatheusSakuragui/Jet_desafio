import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Typography, Card, CardContent, Grid, Button, Tab, Tabs, TableHead, Table, TableCell, TableRow, TableBody } from '@mui/material';
import NavBar from '../components/navBar';
import { saveAs } from 'file-saver';

export default function Leilao() {
    const { id } = useParams();
    const [leilao, setLeilao] = useState(null);
    const [selectedTab, setSelectedTab] = useState(0);

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

    const handleDownload = async () => {
        try {

            const response = await axios.get(`http://localhost:5000/leilaoDET/${leilao.id}`, {
                responseType: 'blob',
            });

            saveAs(response.data, `leilao_${id}.DET`);
        } catch (error) {
            console.error('Erro ao baixar o arquivo:', error);
        }
    };

    const handleTabChange = (event, newValue) => {
        setSelectedTab(newValue);
    };

    if (!leilao) {
        return <div>Carregando...</div>;
    }

    return (
        <>
            <NavBar />
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
                           <Tabs value={selectedTab} onChange={handleTabChange} aria-label="simple tabs example">
                                <Tab label="Veículos" />
                                <Tab label="Eletrônicos" />
                            </Tabs>
                            {selectedTab === 0 && (
                                <Table>
                                    <TableHead>
                                        <TableRow>
                                            <TableCell>Nome</TableCell>
                                            <TableCell>Descrição</TableCell>
                                    
                                        </TableRow>
                                    </TableHead>
                                    <TableBody>
                                        {leilao.produtos.map((produto) => (
                                            produto.veiculo && (
                                                <TableRow key={produto.id}>
                                                    <TableCell><b>{produto.nome}</b></TableCell>
                                                    <TableCell>{produto.descricao}</TableCell>
                                                </TableRow>
                                            )
                                        ))}
                                    </TableBody>
                                </Table>
                            )}

                            {selectedTab === 1 && (
                                <Table>
                                    <TableHead>
                                        <TableRow>
                                            <TableCell>Nome</TableCell>
                                            <TableCell>Descrição</TableCell>
                                        </TableRow>
                                    </TableHead>
                                    <TableBody>
                                        {leilao.produtos.map((produto) => (
                                            produto.eletronico && (
                                                <TableRow key={produto.id}>
                                                    <TableCell><b>{produto.nome}</b></TableCell>
                                                    <TableCell>{produto.descricao}</TableCell>
                                                </TableRow>
                                            )
                                        ))}
                                    </TableBody>
                                </Table>
                            )}



                        </CardContent>
                        <Button variant="contained" onClick={handleDownload}>
                                Download do Leilão
                            </Button>
                    </Card>
                </Grid>
            </Grid>
        </>
    );
}
