/*
  함수를 정의하는 3가지 방법
  1. 선언식
  2. 표현식
    1. function
    2. => (arrow function)
*/

// 1. 선언식 function 함수이름 () {}  === 기명함수
function add(x, y) {
  return x + y
}

let a = add(3, 4)
console.log(a)

// 2. 표현식 === 익명함수를 어떤 함수 식별자에 할당해서 정의
const sub = function (x, y) {
  return x - y
}

let b = sub(4, 3)
console.log(b)


// 3. arrow function
/* 
1. function 키워드를 지운다.
2. () 와 {} 사이에 => 를 넣는다.
--
3. 인자가 딱 1개라면, 괄호 생략 가능
4. 블록 안에 return 구문만 있으면 {} 와 return 모두 삭제 가능

* function(){} vs () => {}
내부에 this 키워드가 있으면 다르게 동작. 이외에는 모두 같음
*/

// 원래는 이거였음
let cube = function (n) {return n**3}

// cube = (n) => {return n**3}
cube = n => n**3
let mul = (x, y) => x*y

// Default Arguments
function withOutDefaultArg(a, b) {
  if (a === undefined) {
    a = 0
  }
  if (b === undefined) {
    b = 0
  }
  return a + b
}

function withDefaultArg(a=0, b=0) {
  return a + b
}