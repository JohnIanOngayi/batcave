#!/usr/bin/node

let stocks = {
  fruits: ["strawberry", "grapes", "banana", "apple"],
  liquids: ["water", "ice"],
  holders: ["cone", "cup", "stick"],
  toppings: ["chocolate", "peanuts"],
};

let is_open = true;

function time(ms) {
  return new Promise((resolve, reject) => {
    if (is_open) {
      setTimeout(resolve, ms);
    } else {
      reject(console.log("Closed"));
    }
  });
}

async function kitchen() {
  try {
  } catch (err) {
    console.log("Lost ", errr);
  } finally {
    console.log("All done");
  }
}

kitchen();
