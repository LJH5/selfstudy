function make101() {
  const myFunc = function (x) {
    return 100 + x 
  }
  return myFunc
}

const asdf = make101()
asdf(1)  // (function(x){return 100 + x})(1)


/* map */
// arr.map( () => {} )
// map(arr, () => {} )

// 일반적으로는, 함수 정의 이후 => 실행
// 실행코드를 먼저 정의(인자 포함)  => 함수를 정의한다.
function map(callback, arr) {
  const newArr = []

  for (const elem of arr) {
    newArr.push(callback(elem))
  }

  return newArr
}

map(function (num) {
  return num + 1
}, [1, 2, 3, 4, 5])




