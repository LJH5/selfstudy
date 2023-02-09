import React, { useState } from "react";
import "../styles/Home.scss";

function Home() {
  let data = [1, 2, 3, 4, 5];

  let [btnActive, setBtnActive] = useState("");

  const toggleActive = (e) => {
    setBtnActive((prev) => {
      return e.target.value;
    });
  };

  return (
    <div className="container">
      {data.map((item, idx) => {
        return (
          <>
            <button
              value={idx}
              className={"btn" + (idx == btnActive ? " active" : "")}
              onClick={toggleActive}
            >
              {item}
            </button>
          </>
        );
      })}
    </div>
  );
}

export default Home;