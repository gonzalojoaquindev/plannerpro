import * as React from 'react';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import { Button, IconButton, MenuItem, Select, TextField } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { AdapterLuxon } from '@mui/x-date-pickers/AdapterLuxon'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import RestoreIcon from '@mui/icons-material/Restore';
import FavoriteIcon from '@mui/icons-material/Favorite';
import LocationOnIcon from '@mui/icons-material/LocationOn';


function Additem(props) {
    const { open, onClose, item } = props;
    const [newItem, setNewItem] = React.useState({
        name: "",
        type: "debito",
        debit: 0,
        credit: 0,
        account: { name: "", id: 8 },
        benefited: 0,
        subcategory: 0
    })
    const [value, setValue] = React.useState(0);
    const [benefited, setBenefited] = React.useState([])
    const [accounts, setAccounts] = React.useState([])
    const [subcategories, setSubcategories] = React.useState([])

    React.useEffect(() => {
        getAccounts()
        getBenefited()
        getSubcategories()
    }, [])

    const getAccounts = async () => {
        const data = await fetch('http://localhost:5000/accounts')
        const accounts = await data.json()
        console.log(accounts)
        setAccounts(accounts)
    }

    const getBenefited = async () => {
        const data = await fetch('http://localhost:5000/benefited')
        const benefited = await data.json()
        console.log(benefited)
        setBenefited(benefited)
    }

    const getSubcategories = async () => {
        const data = await fetch('http://localhost:5000/subcategories')
        const subcategories = await data.json()
        console.log(subcategories)
        setSubcategories(subcategories)
    }






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
    console.log(accounts)

    const handleChange = (e) => {
        const { name, value } = e.target
        setNewItem(prevState => ({
            ...prevState, [name]: value
        }))
        console.log(newItem)
    }

    /* const handleChangeSelect = (event) => {
        setNewItem({
            ...newItem,
            type: event.target.value
        }
        );
    }; */

    const handleChangeSelect = (e) => {
        const { name, value } = e.target
        console.log(e.target)
        setNewItem(estadoPrevio => ({
            ...estadoPrevio, [name]: value
        }))
        console.log(newItem)
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
            <DialogTitle>Agregar nueva transacción {value}</DialogTitle>
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

            <ul>
                {
                    accounts.map((number) =>
                        <li key={number.id}
                            value={number}>{number.name}</li>
                    )
                }
            </ul>


            <Box >
                <BottomNavigation
                    showLabels
                    value={value}
                    onChange={(event, newValue) => {
                        setValue(newValue);
                    }}
                >
                    <BottomNavigationAction label="Gasto" />
                    <BottomNavigationAction label="Ingreso" />
                    <BottomNavigationAction label="Transferencia" />
                </BottomNavigation>
            </Box>



            <TextField
                required
                id="name"
                name="name"
                label="Nombre"
                variant="filled"
                onChange={handleChange}
            />
            <Select
                name="account"
                labelId="account"
                id="account"
                label="Cuenta"
                value={newItem.account}
                variant="filled"
                onChange={handleChange}>
                {
                    accounts.map((account) =>
                        <MenuItem key={account.id} value={account.id}>{account.name}</MenuItem>
                    )
                }

            </Select>
            <Select
                name="benefited"
                id="benefited"
                label="Beneficiado"
                value={newItem.benefited}
                variant="filled"
                onChange={handleChange}>
                {
                    benefited.map((benefited) =>
                        <MenuItem key={benefited.id} value={benefited.id}>{benefited.name}</MenuItem>
                    )
                }

            </Select>
            <Select
                name="category"
                id="category"
                label="Categoria"
                value={newItem.category}
                variant="filled"
                onChange={handleChange}>
                {
                    categories.map((category) =>
                        <MenuItem key={category.id} value={category.id}>{category.name}</MenuItem>
                    )
                }

            </Select>
            <Select
                name="subcategory"
                id="subcategory"
                label="Subcategoria"
                value={newItem.subcategory}
                variant="filled"
                onChange={handleChange}>
                {
                    subcategories.map((subcategory) =>
                        <MenuItem key={subcategory.id} value={subcategory.id}>{subcategory.name}</MenuItem>
                    )
                }

            </Select>
            <Select
                name="type"
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
                <MenuItem value={'cuenta-ahorro'}>Cuenta ahorro</MenuItem>
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