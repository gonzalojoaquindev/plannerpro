import React from 'react';
import { useParams } from 'react-router-dom'

const User = () => {

    // console.log(useParams())
    const { id } = useParams();
    // console.log(id)

    const [usuario, setUsuario] = React.useState({})

    React.useEffect(() => {
        fetchData()
    }, [])

    const fetchData = async () => {
        const data = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        const user = await data.json()
        console.log(user)
        setUsuario(user)
    }

    return (
        <div>
            <h3>{usuario.name}</h3>
            <ul>
                <li>{usuario.username}</li>
                <li>{usuario.email}</li>
                <li>{usuario.phone}</li>
                <li>{usuario.website}</li>
            </ul>
        </div>
    )
}

export default User