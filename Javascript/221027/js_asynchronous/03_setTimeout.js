// 03. 동기, 비동기, 실행 컨텍스트 종합

// 시간 지연 함수 -> 이건 중요하지 않습니다.
function sleep(sec) {
  const delayUntil = Date.now() + sec
  while (Date.now() < delayUntil) {}
}

for (let i = 1; i <= 10; i++) {
  console.log(`${i}번째 반복`)
  sleep(1000)
}

setTimeout(function () {
  console.log("5초 뒤 실행!!")
}, 5000)


// 이 코드의 결과는 무엇일까요?
// 1. "5번째 반복" 문구가 나올 때 "5초 뒤 실행!!"도 같이 나온다.
// 2. "10번째 반복" 문구 이후로 5초가 흐른 다음 "5초 뒤 실행!!"이 나온다.
// 3. "10번째 반복" 문구 이후로 즉시 "5초 뒤 실행!!"이 나온다.
