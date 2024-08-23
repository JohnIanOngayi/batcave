#!/usr/bin/node

let stocks = {
  fruits: ["strawberry", "grapes", "banana", "apple"],
  liquids: ["water", "ice"],
  holders: ["cone", "cup", "stick"],
  toppings: ["chocolate", "peanuts"],
};

let is_open = true;

let order = (time, work) => {
  return new Promise((resolve, reject) => {
    if (is_open) {
      setTimeout(() => {
        resolve(work());
      }, time);
    } else {
      reject(console.log("Sorry, Closed Shop"));
    }
  });
};

order(2000, () => console.log(`${stocks.fruits[0]} was selected`))
  .then(() => {
    return order(0, () => {
      console.log("Production started");
    });
  })
  .then(() => {
    return order(2000, () => {
      console.log("Cutting fruit");
    });
  })
  .then(() => {
    return order(2000, () => {
      console.log(`${stocks.liquids[0]} and ${stocks.liquids[1]} was added`);
    });
  })
  .then(() => {
    return order(1000, () => {
      console.log("The machine was started");
    });
  })
  .then(() => {
    return order(2000, () => {
      console.log(`Package in ${stocks.holders[1]}`);
    });
  })
  .then(() => {
    return order(2000, () => {
      console.log(`${stocks.toppings[1]} was added`);
    });
  })
  .then(() => {
    return order(2000, () => console.log("Icecream is served"));
  })
  .catch(() => {
    console.log("Customer left");
  })
  .finally(() => console.log("All done"));
