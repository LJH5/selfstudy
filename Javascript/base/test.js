// const arr = [1, 2, 3]
// // 필터는 원본이 바뀌지는 않는다
// arr.forEach(function (num) {
//   console.log(num)
// })
// console.log(arr)

// const arr2 = arr.map(function (num) {
//   return num*2
// })
// console.log(arr2)
// // this가 없으면 자유롭게 arrow를 사용하자
// const arr3 = arr.map(num => num*2)
// console.log(arr3)

function withoutSpreadOpr() {
  const odds = [1, 3, 5, 7]
  const evens = [2, 4, 6, 8]
  const nums = odds.concat(evens)
}