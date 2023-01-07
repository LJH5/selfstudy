const lordify = regularPerson => {
  console.log(regularPerson.firstname)
}
var regularPerson = {
  firstname: '홍',
  lastname: '길동'
}

lordify(regularPerson)


const lordify2 = ({firstname}) => {
  console.log(firstname)
}

lordify2(regularPerson)