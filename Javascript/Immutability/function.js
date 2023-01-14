// 원본 변경
function fn1(person) {
  person.name = 'lee'
}
let o1 = { name: 'kim'}
fn1(o1)
console.log(o1) // { name: 'lee' }

//원본 유지
function fn2(person) {
  person = Object.assign({}, person)
  person.name = 'lee'
  return person
}
let o2 = { name: 'kim'}
let o3 = fn2(o2)
console.log(o2, o3) // { name: 'kim' } { name: 'lee' }

//원본 유지
function fn3(person) {
  person.name = 'lee'
}
let o4 = { name: 'kim'}
let o5 = Object.assign({}, o4)
fn3(o5)
console.log(o4, o5) // { name: 'kim' } { name: 'lee' }