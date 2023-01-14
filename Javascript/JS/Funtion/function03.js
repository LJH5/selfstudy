const logCompliment = function(firstname) {
  console.log(`안녕! ${firstname}`)
}
logCompliment('길동')

const createCompliment = function(firstname, message) {
  console.log(`${message}! ${firstname}`)
}
createCompliment('길동', '안녕')

const createCompliment2 = function(firstname, message) {
  return `${message}! ${firstname}`
}
createCompliment('길동', '안녕')