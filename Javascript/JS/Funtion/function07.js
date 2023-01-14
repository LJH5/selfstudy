// 고차 함수
const invokeIf = (condition, fnTrue, fnFalse) =>
  (condition) ? fnTrue() : fnFalse()

const showWelcome = () =>
  console.log('welcome')

const showUnauthorized = () =>
  console.log('Unathorized')

  invokeIf(true, showWelcome, showUnauthorized)
  invokeIf(false, showWelcome, showUnauthorized)