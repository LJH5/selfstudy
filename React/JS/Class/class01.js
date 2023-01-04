function Vacation(des, length) {
  this.des = des
  this.length = length
}

Vacation.prototype.print = function() {
  console.log(`${this.des}는 ${this.length}일 걸립니다.`)
}

const maui = new Vacation('마우이', 7)

maui.print()


// 클래스 만들기
class Vacation2 {
  constructor(des, length) {
    this.des = des
    this.length = length
  }

  print() {
    console.log(`${this.des}는 ${this.length}일 걸립니다.`)
  }
}
const maui2 = new Vacation2('마우이', 7)
maui2.print()


// 상속
class Expedition extends Vacation2 {
  constructor(des, length, gear) {
    super(des, length)
    this.gear = gear
  }

  print() {
    super.print()
    console.log(`당신의 ${this.gear.join('와 당신의')}를 가져오십시오`)
  }
}

const maui3 = new Expedition('마우이', 7, ['선글라스', '카메라'])
maui3.print()