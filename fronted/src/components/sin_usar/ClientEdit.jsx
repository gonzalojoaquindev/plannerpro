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
    const { onClose, selectedValue, open  } = props;
    const [deleteOpen, setDeleteOpen] = React.useState(false)
    const [updatedClient, setUpdatedClient] = React.useState()

    React.useEffect(() => {
        setUpdatedClient(selectedValue)
    }, [])

    console.log(updatedClient)

    const deleteClient = () => {
        setDeleteOpen(true)
    }

    const handleClose = () => {
        onClose(selectedValue);
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
        handleClose()
        try {
            const res = await fetch(`clients_inventory/${id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    name,
                    email,
                    password,
                }),
            });
            const data = await res.json();
            console.log(data);
           /*  setEditing(false);
            setId(""); */
        }
        await getUsers();

        console.log('editado correctamente', updateClient.birthday)

    } catch (e) {
        console.error("Error al editar el cliente: ", e);
        console.log('error', updatedClient)
    }
}


const handleChange = (e) => {
    const { name, value } = e.target
    setUpdatedClient(prevState => ({
        ...prevState, [name]: value
    }))
    console.log(updatedClient)
}



return (
    <Dialog onClose={handleClose} open={open} fullWidth={true} >
        <Grid container alignItems="center">
            <Grid item xs={1}>
                <IconButton
                    aria-label="delete"
                    onClick={() => deleteClient()}
                >
                    <DeleteIcon />
                </IconButton>
            </Grid>
            <Grid item xs={10}>
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
            label="Hostname"
            defaultValue={selectedValue.hostname}
            variant="filled"
            name="hostname"
            onChange={handleChange}
        />
        <TextField
            required
            id="filled-required"
            label="Dirección IP"
            defaultValue={selectedValue.inventory_ip}
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