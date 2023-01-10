import { createSlice } from "@reduxjs/toolkit"

const name = "board"

const initialState = {
  boardList: [],
}

const reducers = {
  getBoardList: (state, action) => {},
  getboardListSuccess: (state, action) => {},
  getBoardListFail: (state, action) => {},
}

const boardSlice = createSlice({
  name,
  initialState,
  reducers,
})

export const boardReducer = boardSlice.reducer
export const boardActions = boardSlice.actions