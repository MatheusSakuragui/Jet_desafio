import * as React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';


const defaultTheme = createTheme();

export default function Cadastro() {
    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        const body = {
            email: data.get('email'),
            senha: data.get('senha'),
            cpf: data.get('cpf'),
            nome: data.get('nome'),
            telefone: data.get('telefone'),
        }
        axios.post('http://localhost:5000/clientes', body)
            .then((response) => {
                console.log(response);
                navigate("/");
            }, (error) => {
                console.log(error);
            });

    };

    return (
        <ThemeProvider theme={defaultTheme}>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box
                    sx={{
                        marginTop: 15,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}
                >
                    <Typography component="h1" variant="h4">
                        Realize seu cadastro
                    </Typography>
                    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email"
                            name="email"
                            autoComplete="email"
                            autoFocus
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="nome"
                            label="Nome"
                            type="text"
                            id="nome"
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="senha"
                            label="Senha"
                            type="password"
                            id="senha"
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="telefone"
                            label="Telefone"
                            type="text"
                            id="telefone"
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="cpf"
                            label="CPF"
                            type="text"
                            id="cpf"
                        />
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            Cadastrar
                        </Button>
                        <Grid container>
                            <Grid item>
                                <Link onClick={() => navigate("/")} variant="body2">
                                    {"Já tem uma conta? Faça login"}
                                </Link>
                            </Grid>
                        </Grid>
                    </Box>
                </Box>

            </Container>
        </ThemeProvider>
    );
}