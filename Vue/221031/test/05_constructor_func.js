const member = {
  name: 'aiden',
  age: 22,
  sId: 2022311491,
}
console.log(member)

const member2 = {
  name: 'haley',
  age: 20,
  sId: 2022311492,
}
console.log(member2)

// 생성자 함수
function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}

const member3 = new Member('issac', 21, 2022654321)
console.log(member3)