import { map } from 'ramda'
import { all, fork } from "redux-saga/effects"
import boardSage from './sagas/boardSaga'

let combineSagas = {}
combineSagas = Object.assign(combineSagas, { boardSage }) // 수정부분

// rootSaga는 반드시 제네레이터로 보낸다
export default function* rootSaga() {
    yield all(map(fork, combineSagas))
}