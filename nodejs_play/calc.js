#!/usr/bin/node

const add = (x, y) => {
  if (x < 0) console.error("Nooooo");
  else return x + y;
};

add(1, 2);
