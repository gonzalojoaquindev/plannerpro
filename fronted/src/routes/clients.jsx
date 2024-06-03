import React from 'react'
import ClientList from '../components/ClientList';
import { DataGrid } from '@mui/x-data-grid';


const clients = () => {
    const rows = [
        { id: 1, col1: 'Hello', col2: 'World' },
        { id: 2, col1: 'DataGridPro', col2: 'is Awesome' },
        { id: 3, col1: 'MUI', col2: 'is Amazing' },
    ];

    [{
        'ap': 'CM05-MAP-01',
        'hostname': 'Pala 1',
        'ip': '10.16.42.159',
        'mac': '00:30:1a:4e:dd:45',
        'rssi': -50,
        'snr': 25,
        'ssid': 'ANTUMESH'
    },
    {
        'ap': 'CM014-MAP-01',
        'hostname': 'Pala 2',
        'ip': '10.16.42.160',
        'mac': '00:30:1a:4e:da:46',
        'rssi': -70,
        'snr': 18,
        'ssid': 'ANTUMESH'
    },
    {
        'ap': 'CM04-MAP-01',
        'hostname': 'Pala 4',
        'ip': '10.16.42.158',
        'mac': '00:30:1a:4e:dd:47',
        'rssi': -68,
        'snr': 8,
        'ssid': 'ANTUMESH'
    }]

    const columns = [
        { field: 'col1', headerName: 'Hostname', width: 150 },
        { field: 'col2', headerName: 'IP', width: 150 },
        { field: 'col3', headerName: 'ap', width: 150 },
        { field: 'col4', headerName: 'ssid', width: 150 },
        { field: 'col5', headerName: 'rssi', width: 150 },
        { field: 'col6', headerName: 'snr', width: 150 },
    ];
    return (
        <>
            {/*  <ClientList /> */}
            <h3>Palas</h3>
            <div style={{ height: 250, width: '100%' }}>
                <DataGrid rows={rows} columns={columns} />
            </div>


        </>
    )
}


export default clients
