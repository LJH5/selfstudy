import { createSlice } from "@reduxjs/toolkit"

const name = "board"

const initialState = {
  boardList: [],
}

const reducers = {
  getBoardList: (state, action) => {}, // view에서 호출
  getboardListSuccess: (state, action) => {}, // saga에서 api 연결 성공시 return 값 적용
  getBoardListFail: (state, action) => {}, // api 연결 실패시 return 값 적용
}

const boardSlice = createSlice({
  name,
  initialState,
  reducers,
})

export const boardReducer = boardSlice.reducer
export const boardActions = boardSlice.actions