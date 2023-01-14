// 오류발생, const는 상수를 선언 값 재할당이 불가능
const pizza = true
pizza = false

// 오류발생, const는 상수를 선언 값 재할당이 불가능
for (const i=0; i<5; i++) {
  console.log(i)
}