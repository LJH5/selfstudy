let o1 = { name: 'kim', score: [1, 2] }
Object.freeze(o1)
o1.name = 'lee'
// 프로퍼디의 객체는 얼리지 못함
o1.score.push(3)
console.log(o1)
Object.freeze(o1.score)
o1.score.push(4)
console.log(o1)