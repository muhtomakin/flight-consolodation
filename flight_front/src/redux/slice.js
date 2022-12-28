import { createSlice } from "@reduxjs/toolkit";
import dayjs from 'dayjs';
import { getDataAsync, iataCodeTurn } from "./service";

export const slice = createSlice({
    name: 'data',
    initialState: {
        today: dayjs(new Date()).toJSON(),
        items: [],
        allCities: [],
        isLoading: false,
        error: null,
        departureCity: '',
        arrivalCity: '',
        userDate: dayjs(new Date()),
        itemShow: 'Flight',
        isSearching: false,
    },
    reducers: {
        changeDatas: (state, action) => {
            state.departureCity = action.payload.departureCity;
            state.arrivalCity = action.payload.arrivalCity;
        },
        changeDataShow: (state, action) => {
            state.itemShow = action.payload;
        }
    },
    extraReducers: {
        [getDataAsync.pending]: (state) => {
            state.isLoading = true;
        },
        [getDataAsync.fulfilled]: (state, action) => {
            state.items = action.payload;
            state.isLoading = false;
            state.isSearching = true;
        },
        [getDataAsync.rejected]: (state, action) => {
            state.isLoading = false;
            state.error = action.error.message;
        },
        [iataCodeTurn.fulfilled]: (state, action) => {
            state.allCities = action.payload;
        },
    }
});

export const {  
    changeDatas,
    changeDataShow
} = slice.actions;

export default slice.reducer;