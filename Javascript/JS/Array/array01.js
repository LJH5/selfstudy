const sandwich = {
  bread: "플랫 브래드",
  meat: "불고기",
  cheese: "모짜렐라",
  toppings: ["오이", "양상추", "올리브"]
}

// const {bread, meat} = sandwich
// console.log(bread, meat)

let {bread, meat} = sandwich
console.log(bread, meat)

bread = "화이트 브래드"
meat = "참치"

console.log(bread, meat)

console.log(sandwich.bread, sandwich.meat)

