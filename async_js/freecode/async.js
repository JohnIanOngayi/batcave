#!/usr/bin/node

let stocks = {
  fruits: ["strawberry", "grapes", "banana", "apple"],
  liquids: ["water", "ice"],
  holders: ["cone", "cup", "stick"],
  toppings: ["chocolate", "peanuts"],
};

let is_open = true;

let toppings_choice = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(console.log("Choose Toppings"));
    }, 3000);
  });
};

async function kitchen() {
  console.log("A");
  console.log("B");
  console.log("C");
  await toppings_choice();
  console.log("D");
  console.log("E");
}

kitchen();

console.log("Doing the dishes");
console.log("Setting the tables");
console.log("Taking other orders");
