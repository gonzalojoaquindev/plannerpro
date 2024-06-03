import * as React from 'react';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import EventIcon from '@mui/icons-material/Event';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import PeopleIcon from '@mui/icons-material/People';
import BarChartIcon from '@mui/icons-material/BarChart';
import LayersIcon from '@mui/icons-material/Layers';
import { Link as LinkRoute } from "react-router-dom";
import { Collapse, List } from '@mui/material';
import StarBorder from '@mui/icons-material/StarBorder';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import StoreIcon from '@mui/icons-material/Store';
import ContentCutIcon from '@mui/icons-material/ContentCut';
import SettingsIcon from '@mui/icons-material/Settings';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';
import DeviceHubIcon from '@mui/icons-material/DeviceHub';
import SignalWifi2BarIcon from '@mui/icons-material/SignalWifi2Bar';
import TapAndPlayIcon from '@mui/icons-material/TapAndPlay';
import PlaceIcon from '@mui/icons-material/Place';
import StorageIcon from '@mui/icons-material/Storage';
import PodcastsIcon from '@mui/icons-material/Podcasts';
import CellTowerIcon from '@mui/icons-material/CellTower';
import AssessmentIcon from '@mui/icons-material/Assessment';

export const MainListItems = () => {
    const [open, setOpen] = React.useState(false);

    const handleClick = () => {
        setOpen(!open);
    };
    return (
        <>
            <LinkRoute to={`monitor-mesh`}>
                <ListItemButton>
                    <ListItemIcon>
                        <AssessmentIcon />
                    </ListItemIcon>
                    <ListItemText primary="Monitoreo Red Mesh" color='primary' />
                </ListItemButton>
            </LinkRoute>
            <LinkRoute to={`mesh-tree`}>
                <ListItemButton>
                    <ListItemIcon>
                        <DeviceHubIcon />
                    </ListItemIcon>
                    <ListItemText primary="Arbol Mesh" />
                </ListItemButton>
            </LinkRoute>
            < LinkRoute to={`signal`}>
                <ListItemButton>
                    <ListItemIcon>
                        <SignalWifi2BarIcon />
                    </ListItemIcon>
                    <ListItemText primary="Niveles de señal" color='primary' />
                </ListItemButton>
            </LinkRoute >
            <LinkRoute to={`clients`}>
                <ListItemButton>
                    <ListItemIcon>
                        <TapAndPlayIcon />
                    </ListItemIcon>
                    <ListItemText primary="Clientes" />
                </ListItemButton>
            </LinkRoute>
            <LinkRoute to={`map`}>
                <ListItemButton>
                    <ListItemIcon>
                        <PlaceIcon />
                    </ListItemIcon>
                    <ListItemText primary="Ubicación de AP" />
                </ListItemButton>
            </LinkRoute>
            <ListItemButton>
                <ListItemIcon>
                    <BarChartIcon />
                </ListItemIcon>
                <ListItemText primary="Analitycs" />
            </ListItemButton>
            <ListItemButton onClick={handleClick}>
                <ListItemIcon>
                    <StorageIcon />
                </ListItemIcon>
                <ListItemText primary="Inventario" />
                {open ? <ExpandLess /> : <ExpandMore />}
            </ListItemButton>
            <Collapse in={open} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                    {/* <ListItemButton sx={{ pl: 4 }}>
                        <ListItemIcon>
                            <ReceiptLongIcon />
                        </ListItemIcon>
                        <ListItemText primary="Servicios" />
                    </ListItemButton> */}
                    <LinkRoute to={`aps_inventory`}>
                        <ListItemButton sx={{ pl: 4 }}>
                            <ListItemIcon>
                                <PodcastsIcon />
                            </ListItemIcon>
                            <ListItemText primary="Acces Point" />
                        </ListItemButton>
                    </LinkRoute>
                    <LinkRoute to={`clients_inventory`}>
                        <ListItemButton sx={{ pl: 4 }}>
                            <ListItemIcon>
                                <TapAndPlayIcon />
                            </ListItemIcon>
                            <ListItemText primary="Clientes" />
                        </ListItemButton>
                    </LinkRoute>
                </List>
            </Collapse>
            <ListItemButton>
                <ListItemIcon>
                    <SettingsIcon />
                </ListItemIcon>
                <ListItemText primary="Configuración" />
            </ListItemButton>


        </>
    )
}

export default MainListItems
