import * as React from 'react';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import { Button, Grid, IconButton, TextField } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import DeleteIcon from '@mui/icons-material/Delete';
import DeleteClient from './ClientDelete';


export default function EditClient(props) {
    const { onClose, selectedValue, open, clientUpdated } = props;
    const [deleteOpen, setDeleteOpen] = React.useState(false)
    const [isRegistered, setIsRegistered] = React.useState(false)
    const [client, setClient] = React.useState({
        hostname: "",
        inventory_ip: "",
        service: "",
        tag: "",
        equipment: ""
    })

    console.log(selectedValue)
    console.log("client", client)
    console.log(isRegistered)
    console.log(clientUpdated)

    React.useEffect(() => {
        getClient()
    }, [selectedValue])


    const handleClose = () => {
        onClose(client);
        getClient()
    };

    const handleCloseDelete = () => {
        setDeleteOpen(false)
    }


    const getClient = async () => {
        try {
            const ip = selectedValue.data.data.ip
            const data = await fetch(`http://localhost:5000/clients_inventory/ip/${ip}`)
            console.log("solicitud correcta?", data.ok)
            const client = await data.json()
            console.log(client)
            if (client.data === 'Dispositivo no registrado') {
                console.log("Cliente no registrado")
                setIsRegistered(false)
                setClient({
                    hostname: "",
                    inventory_ip: ip,
                    service: "",
                    tag: "",
                    equipment: ""
                })
            } else {
                console.log("Cliente registrado obtenido correctamente")
                setIsRegistered(true)
                setClient(client)
            }

        } catch (e) {
            console.error("Error al obtener el cliente: ", e);
        }
    }

    const addClient = async (ip) => {
        try {
            console.log("Vamos a crear el cliente con ip", ip)
            const res = await fetch(`http://localhost:5000/clients_inventory`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    client
                }
                ),

            });

        } catch (e) {
            console.error("Error al agregar el cliente")
        } finally {
            handleClose()
        }
    }

    const updateClient = async () => {
        try {
            console.log("Actualizando el cliente")
            const id = client._id
            console.log(id)
            console.log(client)

            /*  const res = await fetch(`clients_inventory/${id}`, { */
            const res = await fetch(`http://localhost:5000/clients_inventory/${id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    client
                }
                ),

            });
            console.log('res', res)
        } catch (e) {
            console.error("Error al editar el cliente: ", e);
            console.log('error', e)
        } finally {
            handleClose()
        }
    }

    const handleChange = (e) => {

        const { name, value } = e.target
        setClient(prevState => ({
            ...prevState, [name]: value
        }))

    }


    return (
        <Dialog onClose={handleClose} open={open} fullWidth={true} >
            <Grid container alignItems="center" justifyContent={"center"}>
                {/* <Grid item xs={1} sx={{ padding: '10px' }}>
                    <IconButton
                        aria-label="delete"
                        onClick={() => deleteClient()}
                    >
                        <DeleteIcon />
                    </IconButton>
                </Grid> */}
                <Grid item xs={10} sx={{ padding: '10px' }}>
                    <DialogTitle>
                        {
                            isRegistered ? "Editar ciente"
                                : "Registrar cliente"
                        }

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
                defaultValue={client.hostname}
                variant="filled"
                name="hostname"
                onChange={handleChange}
            />
            <TextField
                required
                id="filled-required"
                label="Dirección IP"
                defaultValue={client.inventory_ip}
                variant="filled"
                name="ip"
                onChange={handleChange}
            />
            <TextField
                required
                label="Servicio"
                defaultValue={client.service}
                variant="filled"
                name="service"
                onChange={handleChange}
            />
            <TextField
                required
                label="TAG"
                defaultValue={client.tag}
                variant="filled"
                name="tag"
                onChange={handleChange}
            />
            <TextField
                required
                label="Equipo"
                defaultValue={client.equipment}
                variant="filled"
                name="equipment"
                onChange={handleChange}
            />


            {
                isRegistered ? <Button onClick={updateClient}>Guardar</Button>
                    : <Button onClick={addClient}>Agregar</Button>
            }

            <DeleteClient
                selectedValue={selectedValue}
                open={deleteOpen}
                onClose={handleClose}
                onCloseDelete={handleCloseDelete} />
        </Dialog >

    );
}