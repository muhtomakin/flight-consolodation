import axios from "axios";
import { createAsyncThunk } from "@reduxjs/toolkit";

export const getDataAsync = createAsyncThunk(
    'data/getDataAsync',
    async (props) => {
        const res = await axios.get(`http://127.0.0.1:8000/api/detail/${props.cities}/${props.date}`);
        return res.data;
    }
)

export const iataCodeTurn = createAsyncThunk(
    'data/iataCodeTurn',
    async () => {
        const res = await axios.get('http://127.0.0.1:8000/api/cities');
        return res.data;
    }
)