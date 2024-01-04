import { AppBar, Button, Toolbar, Tooltip } from "@mui/material";
import LogoutOutlinedIcon from '@mui/icons-material/LogoutOutlined';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import { useEffect } from "react";


export default function NavBar(){
    const navigate = useNavigate();

    useEffect(() => {
        Cookies.get('user') ? console.log('Usuário logado') : navigate("/");
    }, [Cookies.get("user")]);

    return(
        <AppBar position="relative">
        <Toolbar>
            <Button color="inherit"><Tooltip title="Minha Conta"> <AccountCircleIcon sx={{ fontSize: 35 }} /> </Tooltip></Button>
            <Button color="inherit" sx={{ ml: 'auto' }} onClick={()=>{navigate("/"); Cookies.remove("user")}}> <Tooltip title="Sair"> <LogoutOutlinedIcon sx={{ fontSize: 35 }} /> </Tooltip></Button>
        </Toolbar>
    </AppBar>
    )
}