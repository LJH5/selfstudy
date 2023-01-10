import React from 'react'
import { Link } from 'react-router-dom'

function Board() {
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