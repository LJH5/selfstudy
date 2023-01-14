// 제대로 실행됨
hey();

function hey() {
  console.log('저기요!')
}


// 오류 발생
hey2();

const hey2 = function() {
  console.log('저기요2!')
}