import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { useSelector } from 'react-redux';
import { bull } from './utils';

export default function Flight() {
    const items = useSelector(state => state.data.items);

    return (
        <Box sx={{ minWidth: 275 }}>
            <h1>
                Flights
            </h1>
            {items?.Flights.map(flight => (
                <Card variant="outlined">
                    <CardContent>
                        <Typography variant="h5" component="div">
                            Travel Company {bull} <span>{flight.TravelCompany}</span>
                        </Typography>
                        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>     
                            Time {bull} <span>{flight.Time}</span>
                        </Typography>
                        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>     
                            Stops {bull} <span>{flight.Stops}</span>
                        </Typography>
                        <Typography sx={{ mb: 1.5 }} color="text.secondary">
                            Duration {bull} <span>{flight.Duration}</span>
                        </Typography>
                        <Typography variant="body2">
                            Price {bull} <span>{flight.Price}</span>
                        </Typography>
                    </CardContent>
                </Card>
            ))}  
        </Box>
    );
}
