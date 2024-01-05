import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';
import DownloadForOfflineIcon from '@mui/icons-material/DownloadForOffline';
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft';
import GavelOutlinedIcon from '@mui/icons-material/GavelOutlined';
import InfoIcon from '@mui/icons-material/Info';
import { Typography, Card, CardContent, Grid, Tab, Tabs, TableHead, Table, TableCell, TableRow, TableBody, IconButton, Divider, Tooltip, DialogActions, Button, DialogTitle, DialogContent, Dialog, TextField } from '@mui/material';
import NavBar from '../components/navBar';
import { saveAs } from 'file-saver';
import Cookies from 'js-cookie';

export default function Leilao() {
    const { id } = useParams();
    const [leilao, setLeilao] = useState(null);
    const [selectedTab, setSelectedTab] = useState(0);
    const [currentTime, setCurrentTime] = useState(new Date());
    const [selectedProduct, setSelectedProduct] = useState(null);
    const [openModal, setOpenModal] = useState(false);
    const [openLanceModal, setOpenLanceModal] = useState(false);
    const [lanceValue, setLanceValue] = useState('');
    const [refresh, setRefresh] = useState(false);
    const user = JSON.parse(Cookies.get('user'));
    const navigate = useNavigate();

    useEffect(() => {
        const timer = setInterval(() => {
            setCurrentTime(new Date());
        }, 1000);

        return () => {
            clearInterval(timer);
        };
    }, []);

    useEffect(() => {
        const fetchLeilao = async () => {
            try {
                const response = await axios.get(`http://localhost:5000/leilao/${id}`);
                setLeilao(response.data);
                setRefresh(false);
            } catch (error) {
                console.error(error);
            }
        };

        fetchLeilao();
    }, [id, refresh]);

    const handleOpenModal = (product) => {
        setSelectedProduct(product);
        setOpenModal(true);
    };

    const handleCloseModal = () => {
        setSelectedProduct(null);
        setOpenModal(false);
    };

    const handleOpenLanceModal = (produto) => {
        setSelectedProduct(produto);
        setOpenLanceModal(true);
    };

    const handleCloseLanceModal = () => {
        setSelectedProduct(null);
        setOpenLanceModal(false);
        setLanceValue('');
    };

    const handleLance = () => {
        const valorLance = parseFloat(lanceValue);
        console.log(selectedProduct)
        if (valorLance < selectedProduct.lance_inicial) {
            alert(`O valor do lance deve ser maior ou igual a ${selectedProduct.lance_inicial}`);
            return;
        } else if (valorLance < selectedProduct.lance_adicional) {
            alert(`O valor do lance deve ser maior ou igual a ${selectedProduct.lance_adicional}`);
            return;
        }

        let body = {
            "valor": valorLance,
            "cliente_id": user.user_id,
            "leilao_id": id,
            "produto_id": selectedProduct.id
        }
        console.log(body)

        axios.post('http://localhost:5000/lance', body).then((response) => {
            alert('Lance realizado com sucesso!');
            setRefresh(true);
        }).catch((error) => {
            if (error.response.status === 401) {
                alert('Erro ao realizar lance!');
            }
            console.log(error);
        });

        console.log('Lance válido:', valorLance);
        handleCloseLanceModal();

    };

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

    const formatarData = (dateString) => {
        const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' };
        return new Date(dateString).toLocaleString('pt-BR', options);
    };

    const formatarTempoRestante = (tempoRestante) => {
        const horas = Math.floor(tempoRestante / 3600);
        const minutos = Math.floor((tempoRestante % 3600) / 60);
        const segundos = tempoRestante % 60;

        return `${horas.toString().padStart(2, '0')}:${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;
    };

    if (!leilao) {
        return <div>Carregando...</div>;
    }

    return (
        <>
            <NavBar />
            <Grid container spacing={3} justifyContent="center" sx={{ marginTop: 5 }}>
            <IconButton color='primary' aria-label="download" size='large' onClick={() => navigate("/home")} sx={{ position: "absolute", left: "1%", top: "10%", borderRadius: "50%" }}>
                                <ArrowCircleLeftIcon sx={{ fontSize: 55 }} />
                            </IconButton>
                <Grid item xs={12} md={6}>
                    <Card>
                        <CardContent sx={{ textAlign: 'center' }}>
                            <IconButton color='primary' aria-label="download" size='large' onClick={handleDownload} sx={{ position: "absolute", left: "70%", bottom: "80%", borderRadius: "50%" }}>
                                <DownloadForOfflineIcon sx={{ fontSize: 45 }} />
                            </IconButton>

                            <Typography variant="h4" gutterBottom>
                                {leilao.nome}
                            </Typography>

                            <Typography variant="subtitle1" color="textSecondary">
                                <b>Início:</b> {formatarData(leilao.data_futura)}
                            </Typography>

                            <Typography variant="subtitle1" color="textSecondary">
                                <b>Fim:</b> {formatarData(leilao.data_visitacao)}
                            </Typography>

                            {leilao.status === "EM ABERTO" && (
                                <Typography variant="subtitle1" color="blue">
                                    <b>Começa em:</b> {formatarTempoRestante(Math.floor((new Date(leilao.data_futura) - currentTime) / 1000))}
                                </Typography>
                            )}

                            {leilao.status === "EM ANDAMENTO" && (
                                <Typography variant="subtitle1" color="orange">
                                    <b>Termina em:</b> {formatarTempoRestante(Math.floor((new Date(leilao.data_visitacao) - currentTime) / 1000))}
                                </Typography>
                            )}

                            {leilao.status === "FINALIZADO" && (
                                <Typography variant="subtitle1" color="red">
                                    <b>Finalizado</b>
                                </Typography>
                            )}

                            <Divider sx={{ marginTop: 2, marginBottom: 2 }} />

                            <Typography variant="h6" paragraph>
                                <b>Descrição</b>
                            </Typography>

                            <Typography variant="body1">
                                {leilao.detalhes}
                            </Typography>
                            <Divider sx={{ marginTop: 2, marginBottom: 2 }} />

                            <Typography variant="h6" paragraph>
                                <b>Produtos</b>
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
                                            <TableCell>Último Lance</TableCell>
                                            <TableCell>Ações</TableCell>
                                        </TableRow>
                                    </TableHead>
                                    <TableBody>
                                        {leilao.produtos.map((produto) => (
                                            produto.veiculo && (
                                                <TableRow key={produto.id}>
                                                    <TableCell><b>{produto.nome}</b></TableCell>
                                                    <TableCell>{produto.descricao}</TableCell>
                                                    <TableCell>{produto.lance_adicional}</TableCell>
                                                    <TableCell>
                                                        <Tooltip title="Mais informações">
                                                            <IconButton color='primary' onClick={() => handleOpenModal(produto)}>
                                                                <InfoIcon />
                                                            </IconButton>
                                                        </Tooltip>
                                                        {leilao.status === "EM ANDAMENTO" && (

                                                            <Tooltip title="Dar Lance">
                                                                <IconButton color='primary' onClick={() => handleOpenLanceModal(produto)}>
                                                                    <GavelOutlinedIcon />
                                                                </IconButton>
                                                            </Tooltip>
                                                        )}
                                                    </TableCell>
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
                                            <TableCell>Último Lance</TableCell>
                                            <TableCell>Ações</TableCell>
                                        </TableRow>
                                    </TableHead>
                                    <TableBody>
                                        {leilao.produtos.map((produto) => (
                                            produto.eletronico && (
                                                <TableRow key={produto.id}>
                                                    <TableCell><b>{produto.nome}</b></TableCell>
                                                    <TableCell>{produto.descricao}</TableCell>
                                                    <TableCell>{produto.lance_adicional}</TableCell>
                                                    <TableCell>
                                                        <Tooltip title="Mais informações">
                                                            <IconButton color='primary' onClick={() => handleOpenModal(produto)}>
                                                                <InfoIcon />
                                                            </IconButton>
                                                        </Tooltip>
                                                        {leilao.status === "EM ANDAMENTO" && (

                                                            <Tooltip title="Dar Lance">
                                                                <IconButton color='primary' onClick={() => handleOpenLanceModal(produto)}>
                                                                    <GavelOutlinedIcon />
                                                                </IconButton>
                                                            </Tooltip>
                                                        )}
                                                    </TableCell>

                                                </TableRow>
                                            )
                                        ))}
                                    </TableBody>
                                </Table>
                            )}

                            {selectedProduct && (
                                <Dialog open={openModal} onClose={handleCloseModal} maxWidth={"md"} fullWidth={true}>
                                    <DialogTitle>{selectedProduct.nome}</DialogTitle>
                                    <DialogContent>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            <b>Marca:</b> {selectedProduct.marca}
                                        </Typography>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            <b>Modelo:</b> {selectedProduct.modelo}
                                        </Typography>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            <b>Descrição:</b> {selectedProduct.descricao}
                                        </Typography>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            <b>Lance Inicial:</b> {selectedProduct.lance_inicial}
                                        </Typography>
                                        <Typography variant="subtitle1" color="textSecondary">
                                            <b>Lance Adicional:</b> {selectedProduct.lance_adicional}
                                        </Typography>
                                        {selectedProduct.eletronico && (
                                            <Typography variant="subtitle1" color="textSecondary">
                                                <b>Voltagem:</b> {selectedProduct.eletronico.voltagem}
                                            </Typography>
                                        )}
                                        {selectedProduct.veiculo && (
                                            <>
                                                <Typography variant="subtitle1" color="textSecondary">
                                                    <b>Ano:</b> {selectedProduct.veiculo.ano}
                                                </Typography>
                                                <Typography variant="subtitle1" color="textSecondary">
                                                    <b>Quantidade de Portas:</b> {selectedProduct.veiculo.qtd_portas}
                                                </Typography>
                                            </>
                                        )}
                                        <Divider sx={{ marginTop: 2, marginBottom: 2 }} />
                                        <Typography variant="h6" paragraph>
                                            <b>Últimos Lances</b>
                                        </Typography>
                                        <Table>
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell>Cliente</TableCell>
                                                    <TableCell>Valor</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                {selectedProduct.lances?.map((lance) => (
                                                    <TableRow key={lance.id}>
                                                        <TableCell>{lance.cliente_nome}</TableCell>
                                                        <TableCell>{lance.valor}</TableCell>
                                                    </TableRow>
                                                ))}
                                            </TableBody>
                                        </Table>
                                    </DialogContent>
                                    <DialogActions>
                                        <Button onClick={handleCloseModal} color="primary">
                                            Fechar
                                        </Button>
                                    </DialogActions>
                                </Dialog>
                            )}

                            <Dialog open={openLanceModal} onClose={handleCloseLanceModal} maxWidth={"sm"} fullWidth={true}>
                                <DialogTitle>Dar Lance</DialogTitle>
                                <DialogContent>
                                    <Typography variant="subtitle1" >
                                        <b>O lance mínimo é de:</b> R$ {selectedProduct?.lance_inicial > selectedProduct?.lance_adicional ? selectedProduct?.lance_inicial : selectedProduct?.lance_adicional}
                                    </Typography>
                                    <TextField
                                        label="Valor do Lance"
                                        variant="outlined"
                                        fullWidth
                                        type="number"
                                        value={lanceValue}
                                        onChange={(e) => setLanceValue(e.target.value)}
                                    />
                                </DialogContent>
                                <DialogActions>
                                    <Button onClick={handleCloseLanceModal} color="primary">
                                        Cancelar
                                    </Button>
                                    <Button onClick={handleLance} color="primary">
                                        Confirmar Lance
                                    </Button>
                                </DialogActions>
                            </Dialog>
                        </CardContent>
                    </Card>
                </Grid>
            </Grid>
        </>
    );
}
