#!/usr/bin/node

function one(callback) {
  console.log(" Step 1 ");
  callback();
}

function two() {
  console.log(" Step 2 ");
}

one(two);
