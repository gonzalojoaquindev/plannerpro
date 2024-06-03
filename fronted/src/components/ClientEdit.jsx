import * as React from 'react';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import { Button, Grid, IconButton, TextField } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import DeleteIcon from '@mui/icons-material/Delete';
import DeleteClient from './ClientDelete';
import { AdapterLuxon } from '@mui/x-date-pickers/AdapterLuxon'
import { DatePicker, LocalizationProvider } from '@mui/x-date-pickers';
import { DateTime } from "luxon";

export default function EditClient(props) {
    const { onClose, selectedValue, open, getClients } = props;
    const [deleteOpen, setDeleteOpen] = React.useState(false)
    const [updatedClient, setUpdatedClient] = React.useState(
        {
            name: selectedValue.name,
            debit: selectedValue.debit
        }
    )



    React.useEffect(() => {
        setUpdatedClient(selectedValue)
    }, [selectedValue])

    /*  React.useEffect(() => {
         setUpdatedClient(updatedClient)
     }, [updatedClient]) */



    const deleteClient = () => {
        setDeleteOpen(true)
    }

    const handleClose = () => {
        onClose(selectedValue);
        getClients()
    };

    const handleCloseDelete = () => {
        setDeleteOpen(false)
    }

    const handleListItemClick = (value) => {
        onClose(value);
    };

    const saveData = () => {
        handleClose()
        console.log("guardado")

    }


    const updateClient = async () => {
        try {
            const id = updatedClient._id

            /*  const res = await fetch(`clients_inventory/${id}`, { */
            const res = await fetch(`http://localhost:5000/clients_inventory/${id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    updatedClient
                }
                ),

            });
            console.log('res', res)
        } catch (e) {
            console.error("Error al editar el cliente: ", e);
            console.log('error', updatedClient)
        } finally {
            handleClose()
        }

    }

    const handleChange = (e) => {

        const { name, value } = e.target
        setUpdatedClient(prevState => ({
            ...prevState, [name]: value
        }))

    }


    return (
        <Dialog onClose={handleClose} open={open} fullWidth={true} >
            <Grid container alignItems="center" justifyContent={"center"}>
                <Grid item xs={1} sx={{ padding: '10px' }}>
                    <IconButton
                        aria-label="delete"
                        onClick={() => deleteClient()}
                    >
                        <DeleteIcon />
                    </IconButton>
                </Grid>
                <Grid item xs={9} sx={{ padding: '10px' }}>
                    <DialogTitle>Editar dispositivo
                    </DialogTitle>
                </Grid>
                <Grid item xs={1}>
                    <IconButton
                        aria-label="close"
                        onClick={handleClose}
                    >
                        <CloseIcon />
                    </IconButton>

                </Grid>
            </Grid>

            <TextField
                required
                id="filled-required"
                label="name"
                defaultValue={selectedValue.name}
                variant="filled"
                name="name"
                onChange={handleChange}
            />
            <TextField
                required
                id="filled-required"
                label="Dirección IP"
                defaultValue={updatedClient.inventory_ip}
                variant="filled"
                name="ip"
                onChange={handleChange}
            />
            <TextField
                required
                label="Servicio"
                defaultValue={selectedValue.service}
                variant="filled"
                name="service"
                onChange={handleChange}
            />
            <TextField
                required
                label="TAG"
                defaultValue={selectedValue.tag}
                variant="filled"
                name="tag"
                onChange={handleChange}
            />
            <TextField
                required
                label="Equipo"
                defaultValue={selectedValue.equipment}
                variant="filled"
                name="equipment"
                onChange={handleChange}
            />


            <Button onClick={updateClient}>Guardar</Button>
            <DeleteClient
                selectedValue={selectedValue}
                open={deleteOpen}
                onClose={handleClose}
                onCloseDelete={handleCloseDelete} />
        </Dialog >

    );
}