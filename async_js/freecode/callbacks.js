#!/usr/bin/node

let stocks = {
  fruits: ["strawberry", "grapes", "banana", "apple"],
  liquids: ["water", "ice"],
  holders: ["cone", "cup", "stick"],
  toppings: ["chocolate", "peanuts"],
};

let order = (fruitname, call_production) => {
  setTimeout(() => {
    console.log(`Order for ${stocks.fruits[fruitname]} placed`);
    call_production();
  }, 2000);
};

let production = () => {
  setTimeout(() => {
    console.log("Production started");
    cutting();
  }, 0);
};

let cutting = () => {
  setTimeout(() => {
    console.log("Cutting fruit");
    liquidate();
  }, 2000);
};

let liquidate = () => {
  setTimeout(() => {
    console.log(`${stocks.liquids[0]} and ${stocks.liquids[1]} was added`);
    start_machine();
  }, 2000);
};

let start_machine = () => {
  setTimeout(() => {
    console.log("The machine was started");
    select_container();
  }, 1000);
};

let select_container = () => {
  setTimeout(() => {
    console.log(`Packaged in ${stocks.holders[1]}`);
    add_toppings();
  }, 2000);
};

let add_toppings = () => {
  setTimeout(() => {
    console.log(`${stocks.toppings[1]} was added`);
    serve();
  }, 2000);
};

let serve = () => {
  setTimeout(() => {
    console.log("Icecream is served");
  }, 2000);
};

order(0, production);
