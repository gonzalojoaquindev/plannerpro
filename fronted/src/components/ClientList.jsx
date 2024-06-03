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
import AddClient from './ClientAdd';
import EditClient from './ClientEdit';
import { DateTime } from "luxon";
import CableIcon from '@mui/icons-material/Cable';

import "../config"


/* console.log('20-07-1993'
    .setLocale("es")
    .toLocaleString(DateTime.DATE_FULL))
 */
export default function ClientList() {

    const [clients, setClients] = React.useState([])
    const [editOpen, setEditOpen] = React.useState(false);
    const [addOpen, setAddOpen] = React.useState(false)
    const [selectedValue, setSelectedValue] = React.useState(
        {
            name: "Defecto",
            email: "defecto",
            birthday: '01-01-2024'
        }
    );

    const addClient = () => {
        setAddOpen(true)
        console.log(addOpen)
    }

    const handleCloseEdit = (value) => {
        setEditOpen(false);
        setSelectedValue(value);
    };

    const handleCloseAdd = () => {
        setAddOpen(false);
    };

    const handleListItemClick = (value) => {
        setSelectedValue(value)
        setEditOpen(true);
    };

    //para ejecutar la peticion luego de que se rendericen los elementos
    React.useEffect(() => {
        getClients()
    }, [])

    const getClients = async () => {
        const data = await fetch('http://localhost:5000/inventary')
        const clients = await data.json()
        setClients(clients)
        console.log(clients)
    }


    return (
        <>
            <Button onClick={() => addClient()}>Agregar cliente</Button>
            <List sx={{ width: '100%', maxWidth: 400 }}>
                {
                    clients.map(item => (

                        <ListItem alignItems="flex-start" key={item.id}>
                            <ListItemButton onClick={() => handleListItemClick(item)}>
                                <ListItemAvatar >
                                    <Avatar alt="Remy Sharp" src="/static/images/avatar/1.jpg" />
                                </ListItemAvatar>
                                <ListItemText
                                    primary={item.hostname}
                                    secondary={
                                        <>
                                            <Typography
                                                sx={{ display: 'block' }}
                                                color="text.secondary"
                                                component="span"
                                            >
                                                {item.inventary_ip}
                                            </Typography>
                                            {item.parent_default !== "" ? (<Typography
                                                sx={{ display: 'block' }}
                                                color="text.secondary"
                                                component="span"
                                            >
                                                <CableIcon sx={{ color: 'orange' }} />
                                                Padre por defecto: {item.parent_default}
                                            </Typography>) : null}


                                        </>
                                    }

                                />

                            </ListItemButton>
                        </ListItem>
                    ))
                }
            </List >
            <EditClient
                selectedValue={selectedValue}
                open={editOpen}
                onClose={handleCloseEdit} />
            <AddClient
                open={addOpen}
                onClose={handleCloseAdd}
            />
        </>
    );
}

