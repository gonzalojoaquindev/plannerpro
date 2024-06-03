import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { FormControl, IconButton, InputLabel, MenuItem, Select, Stack, TextField } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function CalendarModal(props) {
    const { open, onClose, selectedValue } = props;
    console.log(selectedValue)
    /*   const [open, setOpen] = React.useState(false); */
    const handleClose = () => {
        onClose();
    };

    const saveEvent = () => {
        handleClose()
        console.log("te guardé", newClient)
    }

    const [client, setClient] = React.useState('')
    const [barber, setBarber] = React.useState('')

    const handleChangeClient = (event) => {
        setClient(event.target.value);
    };

    const handleChangeBarber = (event) => {
        setBarber(event.target.value);
    };



    return (
        <div>
            {/*           <Button onClick={handleOpen}>Open modal</Button> */}
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                {/* <IconButton
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
                </IconButton> */}
                <Box sx={style}>
                    <Stack direction="column" spacing={1} component="span">
                        <Typography id="modal-modal-title" variant="h6" component="h2">
                            Nueva reserva
                        </Typography>
                        {/*  <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        
                    </Typography> */}

                        <TextField
                            required
                            name="day"
                            id="22"
                            label="Hora inicio"
                            variant="filled"
                            defaultValue={selectedValue.day}
                        /* onChange={handleChange} */
                        />
                        <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Clientes</InputLabel>
                            <Select
                                labelId="client"
                                id="client"
                                value={client}
                                label="Cliente"
                                variant="filled"
                                onChange={handleChangeClient}
                            >
                                <MenuItem value={'Juliao'}>Juliao</MenuItem>
                                <MenuItem value={'Yuri Boika'}>Yuri Boika</MenuItem>
                                <MenuItem value={'Lorencito'}>Lorenzo Cifuentes</MenuItem>
                            </Select>
                        </FormControl>
                        <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Barbero</InputLabel>
                            <Select
                                labelId="client"
                                id="client"
                                value={barber}
                                label="Cliente"
                                variant="filled"
                                onChange={handleChangeBarber}
                            >
                                <MenuItem value={'Daniel Barboza'}>Daniel Barboza</MenuItem>
                                <MenuItem value={'Gonzalo Aguilera'}>Gonzalo Aguilera</MenuItem>
                                <MenuItem value={'Gonzalo Araya'}>Gonzalo Araya</MenuItem>
                            </Select>


                        </FormControl>
                        <TextField
                            required
                            name="client"
                            id="client"
                            label="Cliente"
                            variant="filled"

                        /* onChange={handleChange} */
                        />
                        <TextField
                            required
                            name="service"
                            id="service"
                            label="Servicio"
                            variant="filled"

                        /* onChange={handleChange} */
                        />
                        <Button onClick={() => saveEvent()}>Guardar</Button>
                    </Stack>
                </Box>
            </Modal>
        </div >
    );
}