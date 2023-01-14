// 오류발생, this는 window(최상위)객체라서 resorts라는 객체가 없음
// const gangwon = {
//   resorts: ['용평', '평창', '강촌', '강릉'],
//   print: function(delay=1000) {
//     setTimeout(function() {
//       console.log(this.resorts.join(','))
//     }, delay)
//   }
// }

// gangwon.print()


// 화살표 함수 안에서 this는 한단계위인 gangwon2 함수임
const gangwon2 = {
  resorts: ['용평', '평창', '강촌', '강릉'],
  print: function(delay=1000) {
    setTimeout(() => {
      console.log(this.resorts.join(','))
    }, delay)
  }
}

gangwon2.print()