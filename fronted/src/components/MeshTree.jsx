import * as d3 from "d3";
import React, { useState, useEffect, useRef } from "react";
import ReplayIcon from '@mui/icons-material/Replay';
import { Collapse, Fab, Grid, IconButton, Paper } from "@mui/material";
import Alert from '@mui/material/Alert';
import CheckIcon from '@mui/icons-material/Check';
import CloseIcon from '@mui/icons-material/Close';
import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import ImageIcon from '@mui/icons-material/Image';
import WorkIcon from '@mui/icons-material/Work';
import BeachAccessIcon from '@mui/icons-material/BeachAccess';
import Typography from '@mui/material/Typography';
import EditIcon from '@mui/icons-material/Edit';
import EditClient from './MeshEditNode';

export default function Tree() {
    const svgRef = useRef();
    const [meshTree, setMeshTree] = React.useState([])
    const [isLoading, setIsLoading] = React.useState(false)
    const [isSuccess, setIsSuccess] = React.useState(false)
    const [isError, setIsError] = React.useState(false)
    const [status, setStatus] = React.useState()
    const [open, setOpen] = useState()
    const [device, setDevice] = useState()
    const [clientUpdated, setClientUpdated] = useState()


    const [editOpen, setEditOpen] = React.useState(false);
    const [selectedValue, setSelectedValue] = React.useState(
        {
            name: "Defecto",
            email: "defecto",
            birthday: '01-01-2024'
        }
    );

    console.log(selectedValue)

    const handleCloseEdit = (value) => {
        setEditOpen(false);
        setOpen(false)
        setSelectedValue(value);
    };

    const handleListItemClick = (value) => {
        setSelectedValue(value)
        setEditOpen(true);
    };

    console.log(device)

    /* console.log(isLoading)
    console.log(meshTree)
    console.log(status) */
    //Para ejecutar la peticion luego de que se rendericen los elementos
    useEffect(() => {
        getTree()
    }, [])


    const handleTooltipClose = () => {
        setOpen(false);
    };

    const handleTooltipOpen = (node, event) => {
        setOpen(true);
        const object = {};
        for (const property of Object.keys(node)) {
            object[property] = node[property];
            object.x = event.clientX
            object.y = event.clientY
        }
        setSelectedValue(object)
        setDevice(object)
        console.log("device", device)
    };


    const getTree = async () => {
        setIsLoading(true)
        setStatus("Conectando con servidor...")
        try {
            setIsError(false)
            const data = await fetch('http://localhost:5000/mesh_tree')
            const res = await data.json()
            console.log(res)
            const status = data.msg
            console.log(status)
            setMeshTree(res.data)
            if (data.ok === true) {
                setStatus(status)
                setIsLoading(false)
                console.log("conexión exitosa", status)
            } else {
                setIsLoading(false)
                setIsError(true)
                setStatus(status)
                console.log("Error en el servidor", status)
                console.log(res.detail)
            }

        }
        catch (e) {
            setStatus("No pude establecer una conexión con el servidor.")
            setIsLoading(false)
            setIsError(true)
            console.log(e)
        }



        /*   const meshTree = await data.json()
          console.log(data.ok)
          setMeshTree(meshTree)
          if (data.ok) {
              setStatus("Conexión exitosa, construyendo árbol Mesh")
              setIsLoading(false)
              setIsSuccess(true)
              console.log(document.getElementById('tree'))
          } else {
              setIsLoading(false)
              setIsError(false)
          } */
        /* console.log(status.status) */
    }

    const reload = () => {
        getTree()
    }



    const chart = () => {
        const width = 928;

        // Compute the tree height; this approach will allow the height of the
        // SVG to scale according to the breadth (width) of the tree layout.
        const root = d3.hierarchy(meshTree);
        const dx = 10;
        const dy = width / (root.height + 1);

        // Create a tree layout.
        const tree = d3.tree().nodeSize([dx, dy]);

        // Sort the tree and apply the layout.
        root.sort((a, b) => d3.ascending(a.data.name, b.data.name));
        tree(root);

        // Compute the extent of the tree. Note that x and y are swapped here
        // because in the tree layout, x is the breadth, but when displayed, the
        // tree extends right rather than down.
        let x0 = Infinity;
        let x1 = -x0;
        root.each(d => {
            if (d.x > x1) x1 = d.x;
            if (d.x < x0) x0 = d.x;
        });

        // Compute the adjusted height of the tree.
        const height = x1 - x0 + dx * 2;
        //esto lo puse yo paa que cuando se vuelta a renderizar, se elimine el árbol anterior
        const clear = d3.select(svgRef.current).selectChildren().remove()

        const svg = d3
            .select(svgRef.current)
            .attr("width", width)
            .attr("height", height)
            .attr("viewBox", [-dy / 3, x0 - dx, width, height])
            .attr("style", "max-width: 100%; height: auto; font: 10px sans-serif;");

        const link = svg.append("g")
            .attr("fill", "none")
            /* .attr("stroke", d => d.data.snr !== 0 ? "green" : "red") */
            .attr("stroke", "#B0BEC5")
            .attr("stroke-opacity", 0.4)
            .attr("stroke-width", 1.5)
            .selectAll()
            .data(root.links())
            .join("path")
            .attr("d", d3.linkHorizontal()
                .x(d => d.y)
                .y(d => d.x));


        const node = svg.append("g")
            .attr("stroke-linejoin", "round")
            .attr("stroke-width", 3)
            .selectAll()
            .data(root.descendants())
            .join("g")
            .attr("transform", d => `translate(${d.y},${d.x})`)
            .on("click", (event, node) => {
                /* console.log(d.data) */
                handleTooltipOpen(node, event)
                /* d.children = d.children ? null : d._children;
                update(d); */

            })




        node.append("circle")
            //.attr("fill", d => d.children ? "#555" : "#999")
            .attr("fill", d => d.data.snr !== 0 ? "orange" : "green")
            .attr("r", 3.5)


        node.append("text")
            .attr("fill", "#f5f5f5")
            .attr("dy", "0.31em")
            .attr("x", d => d.children ? -6 : 6)
            .attr("text-anchor", d => d.children ? "end" : "start")
            .text(d => d.data.name)
            .clone(true).lower()
            .attr("stroke", "#263238")
            .attr("stroke-width", 3)
            .attr("stroke-linejoin", "round")
        /*  .on("click", (event, d) => {
             alert("hola")
             d.children = d.children ? null : d._children;
             update(d); 

         })
*/

        return svg.node();
    }
    chart()


    return (
        <>
            {isSuccess && (
                <Collapse in={isSuccess}>
                    <Alert
                        variant="outlined" severity="success"
                        sx={{ mb: 2 }}
                        action={
                            <IconButton
                                aria-label="close"
                                color="inherit"
                                size="small"
                                onClick={() => {
                                    setIsSuccess(false);
                                }}
                            >
                                <CloseIcon fontSize="inherit" />
                            </IconButton>
                        }

                    >
                        Conexión exitosa, Árbol Mesh actualizado
                    </Alert>
                </Collapse>
            )}

            {isError ?
                <Collapse in={isError}>
                    <Alert
                        variant="outlined" severity="error"
                        sx={{ mb: 2, display: "flex", justifyContent: "center", alignItems: "center" }}
                        action={
                            <IconButton
                                aria-label="close"
                                color="inherit"
                                size="small"
                                onClick={() => {
                                    setIsError(false);
                                }}
                            >
                                <CloseIcon fontSize="inherit" />
                            </IconButton>
                        }

                    >
                        {status}
                    </Alert>
                </Collapse> : null}
            <svg width={700} height={600} id="tree" ref={svgRef} />
            <Fab sx={{ position: 'absolute', bottom: 50, right: 50 }} aria-label="recargar" onClick={() => reload()}>
                <ReplayIcon />
            </Fab>

            {isLoading ? (
                <Collapse in={isLoading}>
                    <Alert
                        variant="outlined" severity="info"
                        sx={{ mb: 2 }}
                    >
                        {status}
                    </Alert>
                </Collapse>) : null}


            {open &&
                <Paper sx={{ width: '100%', maxWidth: 300, position: 'absolute', top: device.y, left: device.x }} elevation={4}>
                    <Grid container spacing={2} justifyContent="space-between" alignItems="center" direction="row"
                        sx={{ width: '100%', maxWidth: 300 }}>
                        <Grid item xs>
                            <IconButton
                                aria-label="close"
                                color="inherit"
                                size="small"
                                onClick={() => handleTooltipClose()}
                            >
                                <CloseIcon />
                            </IconButton>
                        </Grid>
                        <Grid item xs={8}>
                            <Typography variant="subtitle1" color="primary" >
                                {device.data.name}
                            </Typography>
                        </Grid>
                        <Grid item xs>
                            <IconButton
                                aria-label="edit"
                                size="small"
                                onClick={() => handleListItemClick(device)}
                            >
                                <EditIcon />

                            </IconButton>
                        </Grid>

                    </Grid>
                    <List >
                        <ListItem>
                            <ListItemAvatar>
                                <Avatar>
                                    <ImageIcon />
                                </Avatar>
                            </ListItemAvatar>
                            <ListItemText>

                                <Typography variant="body2" >
                                    IP: {device.data.data.ip}
                                </Typography>
                                <Typography variant="body2" >
                                    SNR: {device.data.snr}
                                </Typography>
                                <Typography variant="body2" >
                                    Conectado a: {device.parent.data.name}
                                </Typography>
                                {device.data.data.mac &&
                                    <Typography variant="body2" >
                                        MAC: {device.data.data.mac}
                                    </Typography>
                                }


                            </ListItemText>
                        </ListItem>

                    </List>
                </Paper >}


            <Backdrop
                sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
                open={isLoading}
            >
                <CircularProgress color="inherit" />
            </Backdrop>
            <EditClient
                selectedValue={selectedValue}
                open={editOpen}
                onClose={handleCloseEdit}
                clientUpdated={clientUpdated} />
        </>
    )
}

