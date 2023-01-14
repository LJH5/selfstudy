// 함수의 불변성
let color_lawn = {
  title: '잔디',
  color: '#00FF00',
  rating: 0
}

// color 변수의 값을 직접 바꾸지 않음
let rateColor2 = (color, rating) => {
  return Object.assign({}, color, {rating: rating})
}

console.log(rateColor2(color_lawn, 5).rating)
console.log(color_lawn.rating)

// color 변수의 값을 직접 바꿔버림
function rateColor(color, rating) {
  color.rating = rating
  return color
}

console.log(rateColor(color_lawn, 5).rating)
console.log(color_lawn.rating)