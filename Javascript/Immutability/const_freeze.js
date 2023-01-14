const o1 = { name: 'kim'}
Object.freeze(o1)
const o2 = { name: 'lee'}
// o1 = o2 // 오류발생 const는 재할당 불가
o1.name = 'park'
console.log(o1) // { name: 'kim'}, freeze가 값 변화를 막음