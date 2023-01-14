let o1 = { name: 'kim'}
let o2 = { name: 'kim'}

console.log(o1 === o2)

// 같은 곳을 가르킴
let o3 = o1
o3.name = 'lee'
console.log(o1, o3, o1 === o3)

// 다른 곳을 가르킴
let o4 = Object({}, o2)
o4.name = 'lee'
console.log(o2, o4, o2 === o4)