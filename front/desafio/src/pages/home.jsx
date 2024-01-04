import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useEffect, useState } from 'react';
import Cookies from 'js-cookie';
import axios from 'axios';
import { Divider, Tooltip } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import NavBar from '../components/navBar';

const defaultTheme = createTheme();

export default function Album() {
    const [leiloes, setLeiloes] = useState([]);
    const [currentTime, setCurrentTime] = useState(new Date());
    const [filtro, setFiltro] = useState("TODOS");
    const navigate = useNavigate();

    useEffect(() => {
        axios.get('http://localhost:5000/listaleilao').then((response) => {
            setLeiloes(response.data);
        });
    }, []);

    useEffect(() => {
        const timer = setInterval(() => {
            setCurrentTime(new Date());
        }, 1000);

        return () => {
            clearInterval(timer);
        };
    }, []);

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

    const leiloesFiltrados = leiloes.filter((leilao) => {
        if (filtro === "TODOS") {
            return true;
        } else if (filtro === "EM ABERTO") {
            return leilao.status === "EM ABERTO";
        } else if (filtro === "EM ANDAMENTO") {
            return leilao.status === "EM ANDAMENTO";
        } else if (filtro === "FINALIZADO") {
            return leilao.status === "FINALIZADO";
        }
        return false;
    });

    const handleFiltroChange = (novoFiltro) => {
        setFiltro(novoFiltro);
    };

    return (
        <ThemeProvider theme={defaultTheme}>
            <CssBaseline />
          
          <NavBar/>

            <Stack direction="row" spacing={2} sx={{ marginBottom: 2, marginTop: 5, marginLeft: 8 }}>
                <Button variant={filtro === "TODOS" ? "contained" : "outlined"} onClick={() => handleFiltroChange("TODOS")}>
                    Todos
                </Button>
                <Button variant={filtro === "EM ABERTO" ? "contained" : "outlined"} onClick={() => handleFiltroChange("EM ABERTO")}>
                    Em Aberto
                </Button>
                <Button variant={filtro === "EM ANDAMENTO" ? "contained" : "outlined"} onClick={() => handleFiltroChange("EM ANDAMENTO")}>
                    Em Andamento
                </Button>
                <Button variant={filtro === "FINALIZADO" ? "contained" : "outlined"} onClick={() => handleFiltroChange("FINALIZADO")}>
                    Finalizado
                </Button>
            </Stack>

            <Grid container spacing={2}>
                {leiloesFiltrados.map((leilao) => (
                    <Grid item key={leilao.id} xs={12} sm={6} md={4}>
                        <Card variant='outlined'
                            sx={{ display: 'flex', flexDirection: 'column', minHeight: '200px', width: '80%', minWidth: '300px', marginLeft: 8, marginBottom: 5, marginTop: 5 }}
                        >
                            <CardContent sx={{ flexGrow: 1, textAlign: "center" }}>

                                <Typography gutterBottom variant="h3" component="h2">
                                    <b>{leilao.nome}</b>
                                </Typography>

                                <Typography sx={{ fontSize: 20 }}>
                                    {leilao.detalhes}
                                </Typography>

                                <Divider sx={{ marginTop: 2, marginBottom: 2 }} />

                                <Typography>
                                    <b>  Início: </b>  {formatarData(leilao.data_futura)}
                                </Typography>
                                <Typography>
                                    <b> Fim: </b> {formatarData(leilao.data_visitacao)}
                                </Typography>

                                {leilao.status === "EM ANDAMENTO" ? (
                                    <>
                                        <Typography variant="h6" color="text.secondary" paragraph sx={{ color: 'rgba(255, 140, 0, 0.9)' }}>
                                            Tempo Restante: {formatarTempoRestante(Math.floor((new Date(leilao.data_visitacao) - currentTime) / 1000))}
                                        </Typography>

                                    </>
                                ) : null}

                                {leilao.status === "EM ABERTO" ? (
                                    <Typography variant="h6" color="text.secondary" paragraph sx={{ color: 'rgba(0, 0, 255, 0.7)' }}>
                                        Começa em: {formatarTempoRestante(Math.floor((new Date(leilao.data_futura) - currentTime) / 1000))}
                                    </Typography>
                                ) : null}

                                {leilao.status === "FINALIZADO" ? (
                                    <Typography variant="h6" color="text.secondary" paragraph sx={{ color: 'rgba(255, 0, 0, 0.7)' }}>
                                        Finalizado
                                    </Typography>
                                ) : null}
                            </CardContent>
                            <Divider />
                            <CardActions sx={{ justifyContent: 'right', marginTop: 'auto' }}>
                                <Button size="large"><InfoOutlinedIcon sx={{ fontSize: 30 }} onClick={()=> navigate(`/leilao/${leilao.id}`)}/></Button>
                            </CardActions>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </ThemeProvider>
    );
}
