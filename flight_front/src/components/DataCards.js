import { Button, Stack } from '@mui/material'
import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { changeDataShow } from '../redux/slice'
import Car from './Car'
import Flight from './Flight'
import Hotel from './Hotel'

const services = [
    {
        id: 1,
        name: 'Flight',
        service: <Flight />
    },
    {
        id: 2,
        name: 'Hotel',
        service: <Hotel />
    },
    {
        id: 3,
        name: 'Car',
        service: <Car />
    },
]

function DataCards() {
    const dispatch = useDispatch();
    const itemShow = useSelector(state => state.data.itemShow);
    const isSearching = useSelector(state => state.data.isSearching);

    if (isSearching) {
        return (
            <div style={{
                display: 'flex',
                flexDirection: 'column',
                margin: 'auto',
                justifyContent: 'center',
                alignItems: 'center',   
            }} 
            >
                <div style={{
                        display: 'flex',
                        flexDirection: 'row',
                        margin: 'auto',
                        justifyContent: 'center',
                        alignItems: 'center',   
                    }}
                >
                    {services.map((service) => {
                        return (
                            <Stack 
                                key={service.id}
                                direction="row"
                                spacing={3}
                            >
                                <Button 
                                    sx={{
                                        padding: '6px 12px',
                                    }}
                                    variant="contained"
                                    onClick={() => dispatch(changeDataShow(service.name))}
                                >{service.name}</Button>
                            </Stack>
                        );
                    })}
                </div>
                {services.map(service => {
                    if(service.name === itemShow) return service.service 
                })}          
            </div>
        )
    }
}

export default DataCards