import React, { useEffect, useState } from "react"; import { Box, Tab, Tabs, TextField, Button, MenuItem, Select, InputLabel, FormControl } from "@mui/material";
import { format, set } from 'date-fns';
import axios from "axios";

export default function AdmPage() {
    const [value, setValue] = useState(0);
    const [leiloes, setLeiloes] = useState([]); 
    const [refresh, setRefresh] = useState(false); 
    const [formDataLeilao, setFormDataLeilao] = useState({
        nome: "",
        detalhes: "",
        dataInicio: "",
        dataFim: "",
    });
    const [formDataProduto, setFormDataProduto] = useState({
        nome: "",
        marca: "",
        modelo: "",
        descricao: "",
        lanceInicial: "",
        leilaoId: "",
        tipoProdutoId: "",
    });

    function a11yProps(index) {
        return {
            id: `simple-tab-${index}`,
            "aria-controls": `simple-tabpanel-${index}`,
        };
    }

    useEffect(() => {
        axios.get("http://localhost:5000/listaleilao").then((response) => {
            setLeiloes(response.data);
            console.log(response.data);
            setRefresh(false);
        }).catch((error) => {
            console.log(error);
        });
    }, [refresh]);


    const handleSubmitLeilao = (event) => {
        event.preventDefault();

        event.preventDefault();
        const formData = new FormData(event.currentTarget);

        const dataInicio = format(new Date(formData.get("dataInicio")), "yyyy-MM-dd'T'HH:mm:ss");
        const dataFim = format(new Date(formData.get("dataFim")), "yyyy-MM-dd'T'HH:mm:ss");


        const body = {
            nome: formData.get("nome"),
            detalhes: formData.get("detalhes"),
            data_futura: dataInicio,
            data_visitacao: dataFim,
            qtd_produtos: 0,
        };
        console.log(body);
        axios.post("http://localhost:5000/leilao", body).then((response) => {
            console.log(response);
            setRefresh(true);
        }).catch((error) => {
            console.log(error);
        });
        setFormDataLeilao({
            nome: "",
            detalhes: "",
            dataInicio: "",
            dataFim: "",
        });

        alert("Leilão cadastrado com sucesso!");
    };

    const handleSubmitProduto = (event) => {
        event.preventDefault();

        // ... (mesmo código que você já tem)

        // Limpar os campos do formulário de produto
        setFormDataProduto({
            nome: "",
            marca: "",
            modelo: "",
            descricao: "",
            lanceInicial: "",
            leilaoId: "",
            tipoProdutoId: "",
        });
        // Exibir alerta
        alert("Produto cadastrado com sucesso!");
    };


    return (
        <Box sx={{ marginTop: 10, marginLeft: 5, width: "80%" }}>
            <Tabs
                value={value}
                onChange={(event, newValue) => {
                    setValue(newValue);
                }}
                aria-label="basic tabs example"
            >
                <Tab label="Cadastro de Leilão" {...a11yProps(0)} />
                <Tab label="Cadastro Produto" {...a11yProps(1)} />
                <Tab label="Mais um Tab" {...a11yProps(2)} />
            </Tabs>


            <Box role="tabpanel" hidden={value !== 0} id={`simple-tabpanel-${0}`}>
                <Box sx={{ p: 3 }}>
                    <Box component="form" onSubmit={handleSubmitLeilao}>
                        <TextField
                            name="nome"
                            label="Nome"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            value={formDataLeilao.nome}
                            onChange={(e) => setFormDataLeilao({ ...formDataLeilao, nome: e.target.value })}
                        />
                        <TextField
                            name="detalhes"
                            label="Detalhes"
                            fullWidth
                            multiline
                            rows={4}
                            margin="normal"
                            variant="outlined"
                            value={formDataLeilao.detalhes}
                            onChange={(e) => setFormDataLeilao({ ...formDataLeilao, detalhes: e.target.value })}
                        />
                        <TextField
                            name="dataInicio"
                            label="Data de Início"
                            type="datetime-local"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            InputLabelProps={{
                                shrink: true,
                            }}
                            value={formDataLeilao.dataInicio}
                            onChange={(e) => setFormDataLeilao({ ...formDataLeilao, dataInicio: e.target.value })}
                        />
                        <TextField
                            name="dataFim"
                            label="Data de Fim"
                            type="datetime-local"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            InputLabelProps={{
                                shrink: true,
                            }}
                            value={formDataLeilao.dataFim}
                            onChange={(e) => setFormDataLeilao({ ...formDataLeilao, dataFim: e.target.value })}
                        />
                        <Button variant="contained" color="primary" type="submit">
                            Cadastrar Leilão
                        </Button>
                    </Box>
                </Box>
            </Box>

            <Box role="tabpanel" hidden={value !== 1} id={`simple-tabpanel-${1}`}>
                <Box sx={{ p: 3 }}>
                    <Box component="form" onSubmit={handleSubmitProduto}>

                        <TextField
                            name="nomeProduto"
                            label="Nome do Produto"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            value={formDataProduto.nome}
                            onChange={(e) => setFormDataProduto({ ...formDataProduto, nome: e.target.value })}
                        />
                        <TextField
                            name="marcaProduto"
                            label="Marca do Produto"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            value={formDataProduto.marca}
                            onChange={(e) => setFormDataProduto({ ...formDataProduto, marca: e.target.value })}
                        />
                        <TextField
                            name="modeloProduto"
                            label="Modelo do Produto"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            value={formDataProduto.modelo}
                            onChange={(e) => setFormDataProduto({ ...formDataProduto, modelo: e.target.value })}
                        />
                        <TextField
                            name="descricaoProduto"
                            label="Descrição do Produto"
                            fullWidth
                            multiline
                            rows={4}
                            margin="normal"
                            variant="outlined"
                            value={formDataProduto.descricao}
                            onChange={(e) => setFormDataProduto({ ...formDataProduto, descricao: e.target.value })}
                        />
                        <TextField
                            name="lanceInicialProduto"
                            label="Lance Inicial"
                            type="number"
                            fullWidth
                            margin="normal"
                            variant="outlined"
                            value={formDataProduto.lanceInicial}
                            onChange={(e) => setFormDataProduto({ ...formDataProduto, lanceInicial: e.target.value })}
                        />
                        <FormControl fullWidth variant="outlined" margin="normal">
                            <InputLabel id="leilaoIdLabel">Leilão</InputLabel>
                            <Select
                                labelId="leilaoIdLabel"
                                label="Leilão"
                                value={formDataProduto.leilaoId}
                                onChange={(e) => setFormDataProduto({ ...formDataProduto, leilaoId: e.target.value })}
                            >

                                {leiloes.map((leilao) => (
                                    <MenuItem key={leilao.id} value={leilao.id}>
                                        {leilao.nome}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        <FormControl fullWidth variant="outlined" margin="normal">
                            <InputLabel id="tipoProdutoIdLabel">Tipo de Produto</InputLabel>
                            <Select
                                labelId="tipoProdutoIdLabel"
                                label="Tipo de Produto"
                                value={formDataProduto.tipoProdutoId}
                                onChange={(e) => setFormDataProduto({ ...formDataProduto, tipoProdutoId: e.target.value })}
                            >
                                {/* Opções do select para tipo de produto */}
                            </Select>
                        </FormControl>
                        <Button variant="contained" color="primary" type="submit">
                            Cadastrar Produto
                        </Button>
                    </Box>
                </Box>
            </Box>

            {/* Add content for other tabs as needed */}
        </Box>
    );
}
