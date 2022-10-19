// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^
// TypeError: Assignment to constant variable.
// const는 재할당이 불가능 한 변수라서 오류가 발생한다


// 2번
for (num of nums) {
  console.log(num, typeof num)
}
// for in은 객체 순회 -> iterable 순회하는 for of로 바꾼다

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

