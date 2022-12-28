import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { useSelector } from 'react-redux';
import { bull } from './utils';

export default function Car() {
    const items = useSelector(state => state.data.items);

    return (
        <Box sx={{ minWidth: 275 }}>
            <h1>
                Cars
            </h1>
            {items?.Cars.map(car => (
                <Card variant="outlined">
                    <CardContent>
                        <Typography variant="h5" component="div">
                            Car Brand {bull} <span>{car.CarBrand}</span>
                        </Typography>
                        <Typography variant="body2">
                            Daily Price {bull} <span>{car.Price}</span>
                        </Typography>
                    </CardContent>
                </Card>
            ))} 
        </Box>
    );
}
