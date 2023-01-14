// push는 원본 배열을 변화시킴
let list = [
  {title: '빨강'},
  {title: '잔디'},
  {title: '핑크'}
]

const addColor = function(title, colors) {
  colors.push({title: title})
  return colors
}

console.log(addColor('노랑', list))
console.log(list)

console.log('------------------------------------------')

// concat은 원본 배열을 유지
const addColor2 = (title, array) => array.concat({title})
console.log(addColor2('주황', list))
console.log(list)