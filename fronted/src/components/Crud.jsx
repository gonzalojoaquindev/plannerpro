import React, { useState, useEffect } from "react";
import {
    TextField,
    Button,
    Table,
    TableBody,
    TableRow,
    TableCell,
} from "@mui/material";

const MyComponent = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        // Obtener los datos de los usuarios
        fetch("https://jsonplaceholder.typicode.com/users")
            .then((response) => response.json())
            .then((data) => setUsers(data));
    }, []);

    // Agregar un usuario
    const addUser = () => {
        // Crear un nuevo usuario
        const newUser = {
            name: "",
            email: "",
        };

        // Agregar el usuario a la lista de usuarios
        setUsers([...users, newUser]);
    };

    // Editar un usuario
    const editUser = (id) => {
        // Obtener el usuario que se va a editar
        const user = users.find((user) => user.id === id);

        // Mostrar un modal con los datos del usuario
        const [open, setOpen] = useState(false);
        return (
            <Modal open={open} onClose={() => setOpen(false)}>
                <form onSubmit={() => editUserSubmit(id)}>
                    <TextField
                        value={user.name}
                        onChange={(event) => user.name = event.target.value}
                        label="Nombre"
                    />
                    <TextField
                        value={user.email}
                        onChange={(event) => user.email = event.target.value}
                        label="Email"
                    />
                    <Button type="submit">Guardar</Button>
                </form>
            </Modal>
        );
    };

    // Eliminar un usuario
    const deleteUser = (id) => {
        // Eliminar el usuario de la lista de usuarios
        setUsers(users.filter((user) => user.id !== id));
    };

    return (
        <div>
            <h1>Usuarios</h1>
            <Table>
                <TableBody>
                    {users.map((user) => (
                        <TableRow key={user.id}>
                            <TableCell>{user.name}</TableCell>
                            <TableCell>{user.email}</TableCell>
                            <TableCell>
                                <Button onClick={() => editUser(user.id)}>Editar</Button>
                                <Button onClick={() => deleteUser(user.id)}>Eliminar</Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <Button onClick={addUser}>Agregar usuario</Button>
        </div>
    );
};


export default MyComponent;