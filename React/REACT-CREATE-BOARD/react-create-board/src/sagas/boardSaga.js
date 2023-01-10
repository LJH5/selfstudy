import { all, call, fork, put, take } from 'redux-saga/effects'
import { boardActions  } from '../slices/boardSlice'
import axios from '../utils/axios'

// api 서버 연결 주소
function apiGetBoard(boardId) {
  return axios.get(`board/${boardId}`)
}

function apiGetBoardList() {
  return axios.get(`boards`)
}

// api 서버 연결 후 action 호출
async function asyncGetBoardList() {
  try {
    const response = await call(apiGetBoard);
    console.log(response)
  } catch(e) {
    console.error(e)
    await put(boardActions.getBoardListFail(e.response))
  }
}