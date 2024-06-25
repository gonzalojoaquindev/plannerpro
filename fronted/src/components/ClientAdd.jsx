import * as React from 'react';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import { Button, IconButton, MenuItem, Select, TextField } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { AdapterLuxon } from '@mui/x-date-pickers/AdapterLuxon'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';


function Additem(props) {
    const { open, onClose, item } = props;
    const [newItem, setNewItem] = React.useState({
        name: "",
        type: "debito",
        debit: 0,
        credit: 0
    })


    const savenewItem = async () => {
        handleClose()
        try {
            console.log("Se ha creado una nueva cuenta: ", newItem.name);
            console.log(newItem)

            var url = "http://localhost:5000/accounts";
            var data = { username: "example" };

            fetch(url, {
                method: "POST", // or 'PUT'
                body: JSON.stringify(newItem), // data can be `string` or {object}!
                headers: {
                    "Content-Type": "application/json",
                },
            })
                .then((res) => res.json())
                .catch((error) => console.error("Error:", error))
                .then((response) => console.log("Success:", response));



        } catch (e) {
            console.error("Error adding document: ", e);
        }

    }

    const handleChange = (e) => {
        const { name, value } = e.target
        setNewItem(prevState => ({
            ...prevState, [name]: value
        }))
        console.log(newItem)
    }

    const handleChangeSelect = (event) => {
        setNewItem({
            ...newItem,
            type: event.target.value
        }
        );
    };
    const handleChangeDate = (newDate) => {
        setNewItem({
            ...newItem,
            birthday: newDate.toLocaleString()
        })

    }

    const handleClose = () => {
        onClose();
    };




    return (
        <Dialog open={open} fullWidth={true} >

            <DialogTitle>Agregar nuevo item</DialogTitle>
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
            <TextField
                required
                id="name"
                name="name"
                label="Nombre"
                variant="filled"
                onChange={handleChange}
            />
            <Select
                labelId="type"
                id="type"
                label="Tipo"
                value={newItem.type}
                variant="filled"
                onChange={handleChangeSelect}
            >
                <MenuItem value={'debito'}>Debito</MenuItem>
                <MenuItem value={'credito'}>Crédito</MenuItem>
                <MenuItem value={'cuenta-corriente'}>Cuenta Corriente</MenuItem>
                <MenuItem value={'cuenta-corriente'}>Cuenta ahorro</MenuItem>
            </Select>

            <TextField
                required
                name="debit"
                label="Debito"
                variant="filled"
                onChange={handleChange}
            />
            <TextField
                required
                name="credit"
                label="Crédito"
                variant="filled"
                onChange={handleChange}
            />
            <LocalizationProvider
                dateAdapter={AdapterLuxon}
                adapterLocale="en-gb"

            >
                <DatePicker name='birthday' onChange={(newValue) => handleChangeDate(newValue)}

                />
            </LocalizationProvider>

            <Button onClick={() => savenewItem()}>Guardar</Button>
        </Dialog>
    );
}

export default Additem