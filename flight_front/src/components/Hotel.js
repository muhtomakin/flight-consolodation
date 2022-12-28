import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { useSelector } from 'react-redux';
import { bull } from './utils';

export default function Hotel() {
    const items = useSelector(state => state.data.items);

    return (
        <Box sx={{ minWidth: 275 }}>
            <h1>
                Hotels
            </h1>
            {items?.Hotels.map(hotel => (
                <Card variant="outlined">
                    <CardContent>
                        <Typography variant="h5" component="div">
                            Hotel Name {bull} <span>{hotel.HotelName}</span>
                        </Typography>
                        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>     
                            Score {bull} <span>{hotel.Score}</span>
                        </Typography>
                        <Typography sx={{ mb: 1.5 }} color="text.secondary">
                            Reviews {bull} <span>{hotel.Reviews}</span>
                        </Typography>
                        <Typography variant="body2">
                            Price {bull} <span>{hotel.Price}</span>
                        </Typography>
                    </CardContent>
                </Card>
            ))}
            
        </Box>
    );
}
