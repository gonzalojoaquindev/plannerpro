import * as React from 'react';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import DeleteIcon from '@mui/icons-material/Delete';
import { Button, IconButton, TextField } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';




export default function DeleteClient(props) {
    const { onClose, selectedValue, open, onCloseDelete } = props;


    const handleClose = () => {
        onCloseDelete();
        console.log('eliminación cancelada')
    };


    const handleListItemClick = (value) => {
        onClose(value);
    };


    // eliminar el documento de FireStore
    const deleteData = async (id) => {
        /* const clientDoc = doc(db, "clientes", selectedValue.id)
        await deleteDoc(clientDoc) */
        console.log(`cliente ${selectedValue.name} eliminado exitosamente`)
        onCloseDelete()
        onClose()
    }

    return (
        <Dialog onClose={handleClose} open={open} fullWidth={true} >

            <DialogTitle>¿Está seguro de que quiere eliminar el cliente?</DialogTitle>
            <IconButton
                aria-label="close"
                onClick={handleClose}
                sx={{
                    position: 'absolute',
                    right: 8,
                    top: 8,
                    color: (theme) => theme.palette.grey[500],
                }}
            >
                <CloseIcon />
            </IconButton>

            <Button onClick={() => deleteData()}>Eliminar cliente</Button>
        </Dialog>
    );
}