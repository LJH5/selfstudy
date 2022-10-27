// 02. 동기와 비동기

// 동기
console.log("첫 번째")
console.log("두 번째")
console.log("세 번째")

// 비동기
console.log("첫 번째")
setTimeout(() => console.log("두 번째"), 2000)
console.log("세 번째")