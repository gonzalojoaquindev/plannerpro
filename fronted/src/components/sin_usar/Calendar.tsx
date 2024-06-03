import React, { useEffect, useState } from 'react';

import { DateTime } from 'luxon';
import Kalend, { CalendarView, OnEventDragFinish } from 'kalend';
import 'kalend/dist/styles/index.css';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import CalendarModal from './CalendarModal';


const CalendComponent = (props: any) => {




    /*  const [demoEvents, setDemoEvents] = useState([]);
 
   
     useEffect(() => {
         setDemoEvents(generateDemoEvents(DateTime.now(), 80));
     }, []);

     
  */


    const [events, setEvents] = React.useState([
        {
            id: 1,
            startAt: '2024-01-03T15:00:00.000Z',
            endAt: '2024-01-03T19:00:00.000Z',
            timezoneStartAt: 'Europe/Berlin', // optional
            summary: 'Corte de pelo con juliao',
            color: 'blue',
            calendarID: 'work'
        },
        {
            id: 2,
            startAt: '2024-01-03T11:00:00.000Z',
            endAt: '2024-01-03T14:00:00.000Z',
            timezoneStartAt: 'Europe/Berlin', // optional
            summary: 'Lavado de cabeza',
            color: 'green'
        }
    ])

    /* const [clients, setClients] = React.useState([])

    //ara ejecutar la peticion luego de que se rendericen los elementos
    useEffect(() => {
        getClients()
    }, [])

    const getClients = async () => {
        const data = await fetch('https://jsonplaceholder.typicode.com/users')
        const clients = await data.json()
          console.log(clients)
        setClients(clients)

    } */

    const [newEvent, setNewEvent] = React.useState({
        hour: 0.48890625,
        day: 'Wed Jan 03 2024 18: 51: 44 GMT-0300',
        startAt: '2024-01-03T11:00:00.000Z',
        endAt: '2024-01-03T14:00:00.000Z',
        view: 'threeDays',
        event: 'click event',

    })

    console.log(newEvent)

    const onNewEventClick = (data: any) => {
        /*  const msg = `${JSON.stringify({
             hour: data.hour,
             day: data.day,
             startAt: data.startAt,
             endAt: data.endAt,
             view: data.view,
             event: 'click event ',
         })}`; */
        const dateOnClick = {
            hour: data.hour,
            day: data.day,
            startAt: data.startAt,
            endAt: data.endAt,
            view: data.view,
            event: 'click event ',
        };

        console.log('nuevo evento', dateOnClick);
        /*   console.log('data', data); */
        /* setNewEvent(dateOnClick) */
        setOpen(true)

    }



    const addNewEvent = (msg: any) => {
        const updatedEvents = [...events, msg]
        setOpen(true)
        console.log(updatedEvents)
        setEvents(updatedEvents)
        console.log("agregado correctamente")
        console.log("estados de eventos", events)
    }





    const [open, setOpen] = React.useState(false);
    console.log("estado de Open", open)

    /*   const handleClickOpen = () => {
          setOpen(true);
      }; */

    const handleClose = () => {
        setOpen(false);
    };

    // Callback for event click
    const OnEventClick = (data: any) => {
        const msg = `hiciste click en el evento action\n\n Callback data:\n\n${JSON.stringify(data)}`;
        console.log(data);
    }
    /*    handleClickOpen() */


    // Callback after dragging is finished
    /*  const onEventDragFinish: OnEventDragFinish = (
         prev: any,
         current: any,
         data: any
     ) => {
         getClients(data);
     }; */

    return (
        <>
            <Kalend
                kalendRef={props.kalendRef}
                onNewEventClick={onNewEventClick}
                initialView={CalendarView.THREE_DAYS}
                disabledViews={[]}
                onEventClick={OnEventClick}
                events={events}
                initialDate={new Date().toISOString()}
                hourHeight={100}
                showWeekNumbers={true}
                timezone={'Europe/Berlin'}
                draggingDisabledConditions={{
                    summary: 'Computers',
                    allDay: false,
                    color: 'green',
                }}
                //onEventDragFinish={onEventDragFinish}
                onStateChange={props.onStateChange}
                selectedView={props.selectedView}
                showTimeLine={true}
                isDark={true}
                autoScroll={false}
                // disabledDragging={true}
                colors={{
                    light: {
                        primaryColor: 'blue',
                    },
                    dark: {
                        primaryColor: 'orange',
                    },
                }}
            />
            <CalendarModal open={open} selectedValue={newEvent} />
        </>
    );
};


export default CalendComponent;