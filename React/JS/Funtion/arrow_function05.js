const showWelcome = () =>
  console.log('hello')

showWelcome()


const userLogs = userName => message => 
  console.log(`${userName} -> ${message}`)

const log = userLogs('asd123')

log('아바바밥바')