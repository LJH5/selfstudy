const person = (firstName, lastName) => ({
  first: firstName,
  last: lastName
})

console.log(person('길동', '홍'))

// 매개변수와 반환 객체의 이름이 같으면 생략 가능
const person2 = (first, last) => ({
  first,
  last 
})

console.log(person2('길동', '홍'))