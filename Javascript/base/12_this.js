// this

/*
  this 는 아래의 경우를 제외하고 모두 최상위 객체(window)를 bind 된다..
  1. constructor 함수 내부에서 => 생성될 객체를 bind 된다.
  2. '메서드' === (obj.method 로 호출됨) 에서 => 메서드가 소속된 객체(object)를 bind 된다.
    1. Object 에서 Key - function 으로 정의된 것
    2. class 정의 내부의 메서드 정의
*/


const alex = {
  lastName: '권',
  firstName: '이혁',
  greeting: function () {
    return `안녕하세요 ${this.lastName + this.firstName}입니다.`
  }
}

alex.greeting()

/* execution context */

function greeting() {
  console.log(this)
  return `안녕하세요 ${this.lastName + this.firstName}입니다.`
}

const kong = {
  lastName: '공',
  firstName: '형규',
  // greeting: greeting,
  greeting,
}

kong.greeting()  // method true => .greeting() O
greeting()  // method false => .greeting() x

/* Arrow Function */

// without arrow function
const double = {
  numbers: [1, 2, 3, 4],

  x: 2,

  get_double() {
    const doubled = this.numbers.map(function (num) {
      console.log(this)
      return num * this.x
    })   
    // .bind(this)) 
    return doubled
  }
}
double.get_double()  // .map 의 인자 cb 함수는 메서드가 아니다. 고로 cb 안의 this 는 windows 가 된다.


// with Arrow function
const triple = {
  numbers: [1, 2, 3, 4],
  x: 3,

  get_triple() {
    // .map 의 인자 cb 함수는 메서드가 아니지만, Arrow function 으로 표현했기 때문에 this가 원하는 대로 bind 되었다.
    return this.numbers.map(num=> num * this.x)  
  }
}

// 이건 비교 3개
// const neo = {
//   lastname:'유',
//   greeting: function () {
//     console.log(this.lastname)
//   }
// }

// const alex = {
//   lastname:'권',
//   greeting () {
//     console.log(this.lastname)
//   }
// }

// const mj = {
//   lastname:'김',
//   greeting: () => { console.log(this.lastname)}
// } // undefined

// neo.greeting()
// alex.greeting()
// mj.greeting()