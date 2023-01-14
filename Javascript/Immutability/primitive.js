let p1 = 1
let p2 = 1

console.log(p1 === p2)

// 원본 변경 안됨
let p3 = p1
console.log(p1, p3, p1 === p3)
p3 = 2
console.log(p1, p3, p1 === p3)