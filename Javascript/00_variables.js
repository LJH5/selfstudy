// 1. dash-case(kebab-case) => html, css 사용
// 2. snake_case
// 3. camelCase === lowerCamelCase (JS 주로 활용)
// 4. PascalCase === UpperCamelCase (JS class명)
// 5. UPPER_SNAKE_CASE => 절대 변하면 안될 것 같은 상수들

// let = > 변수 선언 방식, 재'할당' 가능 (재선언은 불가능)
let x = 3
x = 4

// const => 안 바뀔만한 것에 쓴다, 재선언 및 재할당 불가능
const y = 3
// y = 12

// var => ES5, 재선언 및 재할당 가능
console.log(foo) // 호이스팅 되어 undefined
var foo;

console.log(bar) // reference error
let bar;