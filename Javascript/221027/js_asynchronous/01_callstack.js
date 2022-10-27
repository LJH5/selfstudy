// 01. 콜스택과 실행 컨텍스트

const foo = function () {
  console.log("foo")
}

const bar = function () {
  console.log("bar")
}

foo()
bar()
