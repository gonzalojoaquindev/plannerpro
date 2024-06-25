import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import { Button, TextField } from '@mui/material';
import EditClient from '../components/ClientEdit';
import { DateTime } from "luxon";
import CableIcon from '@mui/icons-material/Cable';
import "../config"
import AddClient from '../components/ClientAdd';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';


import { DataGrid } from '@mui/x-data-grid';

export default function ClientsInventory() {

    const [clients, setClients] = React.useState([])
    console.log(clients)
    const [editOpen, setEditOpen] = React.useState(false);
    const [selectedValue, setSelectedValue] = React.useState({
        name: "Defecto"
    })
    const [addOpen, setAddOpen] = React.useState(false)



    const addClient = () => {
        console.log("agregando cuenta")
        setAddOpen(true)

    }

    const handleCloseEdit = (value) => {
        setEditOpen(false);
        setSelectedValue(value);
    };

    const handleCloseAdd = () => {
        setAddOpen(false);
    };

    const handleListItemClick = (value) => {
        console.log(value)
        setSelectedValue(value)
        setEditOpen(true);
    };


    //para ejecutar la peticion luego de que se rendericen los elementos
    React.useEffect(() => {
        getClients()
        /*  transform() */
    }, [])

    const getClients = async () => {
        console.log("obteniendo clientes")
        const data = await fetch('http://localhost:5000/accounts')
        const clients = await data.json()
        console.log(clients)
        setClients(clients)
    }

    return (
        <>
            <Button onClick={() => addClient()}>Agregar cuenta</Button>

            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow >
                            <TableCell>ID</TableCell>
                            <TableCell align="center">Nombre</TableCell>
                            <TableCell align="center">Tipo</TableCell>
                            <TableCell align="center">Debito</TableCell>
                            <TableCell align="center">Credito usado</TableCell>
                            <TableCell align="center">editar</TableCell>

                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {clients.map((row) => (
                            <TableRow
                                key={row.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                onClick={() => handleListItemClick(row)}

                            >
                                <TableCell component="th" scope="row">
                                    {row.id}
                                </TableCell>
                                <TableCell align="center">{row.name}</TableCell>
                                <TableCell align="center">{row.type}</TableCell>
                                <TableCell align="center">
                                    {row.debit}</TableCell>
                                <TableCell align="center">
                                    {row.credit_used}
                                </TableCell>
                                <TableCell align="center">
                                    edit
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer >

            <EditClient
                selectedValue={selectedValue}
                open={editOpen}
                onClose={handleCloseEdit}
                getClients={() => getClients()} />

            <AddClient
                open={addOpen}
                onClose={handleCloseAdd}
            />
        </>
    );
}


