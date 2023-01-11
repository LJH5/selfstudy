import { createSlice } from '@reduxjs/toolkit'

const name = 'board'

const initialState = {}

const reducers = {}

const boardSlice = createSlice({
  name,
  initialState,
  reducers
})

export const boardReducer = boardSlice.reducer
export const boardActions = boardSlice.actions