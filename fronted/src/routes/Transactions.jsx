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
import AddClient from '../components/transactions/Add';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';


import { DataGrid } from '@mui/x-data-grid';

export default function Transactions() {

    const [tran, setTran] = React.useState([])
    console.log(tran)
    const [editOpen, setEditOpen] = React.useState(false);
    const [selectedValue, setSelectedValue] = React.useState({
        name: "Defecto"
    })
    const [addOpen, setAddOpen] = React.useState(false)



    const addTran = () => {
        console.log("agregando transacción")
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


    //Para ejecutar la peticion luego de que se rendericen los elementos
    React.useEffect(() => {
        getClients()
        /*  transform() */
    }, [])

    const getClients = async () => {
        console.log("Obteniendo transacciones")
        const data = await fetch('http://localhost:5000/transactions')
        const tran = await data.json()
        console.log(tran)
        setTran(tran)
    }

    return (
        <>
            <h3>Transacciones</h3>
            <Button onClick={() => addTran()}>Agregar transacción</Button>

            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow >
                            <TableCell>fecha</TableCell>
                            <TableCell align="center">Categoria</TableCell>
                            <TableCell align="center">Tipo</TableCell>
                            <TableCell align="center">Cuenta Origen</TableCell>
                            <TableCell align="center">Cuenta destino</TableCell>
                            <TableCell align="center">Gasto</TableCell>
                            <TableCell align="center">Ingreso</TableCell>
                            <TableCell align="center">editar</TableCell>

                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {tran.map((row) => (
                            <TableRow
                                key={row.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                onClick={() => handleListItemClick(row)}

                            >
                                <TableCell component="th" scope="row">
                                    {row.fecha}
                                </TableCell>
                                <TableCell align="center">{row.categoria}</TableCell>
                                <TableCell align="center">{row.Tipo}</TableCell>
                                <TableCell align="center">
                                    {row.cuenta_origen}</TableCell>
                                <TableCell align="center">
                                    {row.cuenta_destino}
                                </TableCell>
                                <TableCell align="center">
                                    {row.Gasto}
                                </TableCell>
                                <TableCell align="center">
                                    {row.Ingreso}
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


