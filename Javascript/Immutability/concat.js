let score = [1, 2, 3]

score.push(4) 
console.log(score) // [ 1, 2, 3, 4 ]

let score2 = score.concat(5)
console.log(score, score2) // [ 1, 2, 3, 4 ] [ 1, 2, 3, 4, 5 ]

let a = score
let b = score

let score3 = score.concat(5)
console.log(score, score3, a, b)