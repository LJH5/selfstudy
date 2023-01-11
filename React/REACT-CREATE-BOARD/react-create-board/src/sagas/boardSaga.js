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
      const response = await call(apiGetBoardList);
      console.log(response)
      if (response?.status === 200) {
        await put(boardActions.getboardListSuccess(response))
      } else {
        await put(boardActions.getBoardListFail(response))
      }
  } catch(e) {
      console.error(e);
      await put(boardActions.getBoardListFail(e.response));
  }
}

// action 호출을 감시하는 watch 함수
async function watchGetBoardList() {
  while(true) {
      await take(boardActions.getBoardList);
      await call(asyncGetBoardList);
  }
}

export default async function boardSaga()
{
  await all([fork(watchGetBoardList)]);
}