let o1 = { name: 'kim', score: [1, 2]}
let o2 = Object.assign({}, o1)
o2.score = o2.score.concat()
console.log(o1 === o2, o1.score === o2.score)
o2.score.push(3)
console.log(o1, o2)