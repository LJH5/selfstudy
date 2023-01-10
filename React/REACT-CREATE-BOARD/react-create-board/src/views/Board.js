import React, { useEffect } from 'react'
import { useDispatch} from 'react-redux'
import { Link } from 'react-router-dom'
import { boardActions } from '../slices/boardSlice'

function Board() {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(boardActions.getBoardList())
  }, [dispatch])
  return (
    <div>
      <ul>
        <li>
          <Link to="/">
            <span>Main</span>
          </Link>
        </li>
        <li>
          <Link to="/board/1">
            <span>board1</span>
          </Link>
        </li>
        <li>
          <Link to="/board/2">
            <span>board2</span>
          </Link>
        </li>
      </ul>
    </div>
  );
}

export default Board