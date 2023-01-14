var regularPerson = {
  firstname: '홍',
  lastname: '길동'
}

const lordify = regularPerson => {
  console.log(regularPerson.firstname)
}

lordify(regularPerson)


const lordify2 = ({firstname}) => {
  console.log(firstname)
}

lordify2(regularPerson)