const lordify = function(firstname) {
  return `안녕! ${firstname}`
}
console.log(lordify('길동'))


// 애로우 메소드로 변경
const lordify2 = firstname => `안녕! ${firstname}`
console.log(lordify2('길동'))