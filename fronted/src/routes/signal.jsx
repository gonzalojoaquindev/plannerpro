import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import LinearProgress from '@mui/material/LinearProgress';
import { red, deepOrange, green, amber, lime } from '@mui/material/colors';



function LinearDeterminate() {
    const [progress, setProgress] = React.useState(0);
    const level = progress > 75 ? "success" : progress > 50 ? "primary" : "error";

    React.useEffect(() => {
        const timer = setInterval(() => {
            setProgress((oldProgress) => {
                if (oldProgress === 100) {
                    return 0;
                }
                const diff = /* Math.random() * */ 10;
                return Math.min(oldProgress + diff, 100);
            });
        }, 1000);

        //ahora qiero simular estas peticiones desde el servidor para que sea más real, poponer el temporizador cada 22 segundos en el fronted y que se simules el rssi desde el backend
        //luego hay que ver como pongo de colores las lineas en le mesh tree

        return () => {
            clearInterval(timer);
        };
    }, []);

    return (
        <Box sx={{ width: '100%' }}>
            <LinearProgress variant="determinate" value={progress} color="primary" />
        </Box>
    );
}

function SimulateRSSI() {

    const [progress, setProgress] = React.useState(-100);


    React.useEffect(() => {
        const timer = setInterval(() => {
            function getRandomInt(min, max) {
                min = Math.ceil(min);
                max = Math.floor(max);
                return Math.floor(Math.random() * (max - min) + min);
            }
            setProgress((oldProgress) => {
                const random = getRandomInt(-100, -20)
                console.log(random)
                return random
                /*  return Math.min(oldProgress + diff, 100); */
            });
        }, 10000);

        return () => {
            clearInterval(timer);
        };
    }, []);

    return (
        <Box sx={{ width: '100%' }}>
            <LinearProgress variant="determinate" value={progress + 100} color={progress + 100 > 35 ? "success" : progress + 100 > 25 ? "primary" : "error"} />
            {progress} {progress + 100}
        </Box>
    );
}


export default function Signal() {
    const [levels, setLevels] = React.useState([])
    const getLevels = async () => {
        const data = await fetch('http://localhost:5000/clients_detail')
        const levels = await data.json()
        setLevels(levels)
        console.log(levels)
    }

    React.useEffect(() => {
        getLevels()
        const timer = setInterval(() => {
            console.log("Solicitando niveles de señal")
            getLevels()
        }, 15000);
    }, [])

    const excellent = green[500]
    const good = lime["A400"]
    const fair = amber[500]
    const poor = deepOrange[500]
    const noSignal = red[800]
    const verde = "#4caf50"

    //
    /*   const formaterLevels = () => {
          if (levels.length === 0) {
              return <div>No signal yet...</div>
          }else {
              console.log("Formateando los detalles del cliente")
              return (
                  
              )
          }
      }
   */
    /*  const snr_color = progress > 75 ? "success" : progress > 50 ? "primary" : "error";
     const rssi_color = progress > 75 ? "success" : progress > 50 ? "primary" : "error"; */

    return (
        <>
            <h3>Palas</h3>
            <LinearDeterminate />
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Hostname</TableCell>
                            <TableCell align="center">IP</TableCell>
                            <TableCell align="center">AP</TableCell>
                            <TableCell align="right">SNR</TableCell>
                            <TableCell align="right">RSSI</TableCell>
                            <TableCell align="right">CANAL</TableCell>

                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {levels.map((row) => (
                            <TableRow
                                key={row.hostname}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell component="th" scope="row">
                                    {row.hostname}
                                </TableCell>
                                <TableCell align="center">{row.ip}</TableCell>
                                <TableCell align="center">{row.ap}</TableCell>
                                <TableCell align="right">
                                    <LinearDeterminate />
                                    {row.snr}</TableCell>
                                <TableCell align="right">
                                    {row.ap}
                                    <LinearProgress variant="determinate" value={row.rssi + 100}
                                        color={row.rssi + 100 > 35 ? "success" : row.rssi + 100 > 25 ? "primary" : "error"} />
                                    {row.rssi} {/* {row.rssi + 100} */}
                                </TableCell>

                                <TableCell align="right">{row.channel}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer >
        </>
    );
}
