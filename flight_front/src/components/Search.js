import * as React from 'react';
import dayjs from 'dayjs';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';
import DatePicker from './DatePicker';
import { useDispatch, useSelector } from 'react-redux';
import { changeDatas } from '../redux/slice';
import { getDataAsync } from '../redux/service';
import { iataCodeTurn } from '../redux/service';

let citiesCode = {
    depCityCode: '',
    arrCityCode: '',
}

export default function Search() {
    const allCities = useSelector(state => state.data.allCities);
    const dispatch = useDispatch();

    React.useEffect(() => {
        dispatch(iataCodeTurn());
    }, [dispatch])

    const [datas, setDatas] = React.useState({
        departureCity: '',
        arrivalCity: '',
        date: dayjs(new Date()),
        userDate: '',

    });

    const handleDatas = () => {  
        allCities.forEach(city => {
            if(city.nameCity.toLowerCase() === datas.departureCity.toLowerCase()) citiesCode.depCityCode = city.codeIataCity;
            if(city.nameCity.toLowerCase() === datas.arrivalCity.toLowerCase()) citiesCode.arrCityCode = city.codeIataCity
        })
        const cities = `${citiesCode.depCityCode}-${citiesCode.arrCityCode}`
        const date = datas.userDate
        dispatch(getDataAsync({cities, date}))
    }

    return (
        <Box
            component="form"
            sx={{
                '& .MuiTextField-root': {
                    m: 3,
                    width: '75ch',
                },
            }}
            noValidate
            autoComplete="off"
        >
            <div style={{ 
                display: 'flex',
                flexDirection: 'row',
                margin: '0 auto',
            }}>
                <TextField
                    id="filled-search"
                    label="Departure City"
                    type="search"
                    variant="filled"
                    onChange={(e) => setDatas({
                        ...datas,
                        departureCity: e.target.value,                       
                    })}
                />
                <TextField
                    id="filled-search"
                    label="Arrival City"
                    type="search"
                    variant="filled"
                    onChange={(e) => setDatas({
                        ...datas,
                        arrivalCity: e.target.value,
                    })}
                />
            
                <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <Stack spacing={3}>
                        <DesktopDatePicker
                        label="Date desktop"
                        inputFormat="MM/DD/YYYY"
                        value={datas.date}
                        onChange={(e) => setDatas({
                            ...datas, 
                            date: e, 
                            userDate: `${e.year()}-${Number(e.month()) >= 10 ? Number(e.month())+1 : `0${String(Number(e.month())+1)}`}-${e.date()}`})}
                        renderInput={(params) => <TextField {...params} />}
                        />
                    </Stack>
                </LocalizationProvider>
                <Stack direction="row" spacing={2}>
                    <Button 
                        sx={{
                            padding: '6px 12px',
                            height: '40%',
                            top: '27px'
                        }}
                        variant="contained"
                        onClick={handleDatas}
                    >Submit</Button>
                </Stack>
            </div>
        </Box>
    );
}