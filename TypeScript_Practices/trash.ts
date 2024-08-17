#!/usr/bin/node

interface Voter {
  name: string;
  age: number;
}

const scores: number[] = [10, 20, 30, 40, 50];
const favoriteThings: string[] = [
  "raindrops on roses",
  "whiskers on kittens",
  "bright copper kettles",
  "warm woolen mittens",
];
const voters: Voter[] = [
  { name: "Joe", age: 22 },
  { name: "Beth", age: 19 },
  { name: "Sam", age: 24 },
];

function getLastItem<T>(array: T[]): T {
  return array[array.length - 1];
}

console.log(getLastItem(scores));
console.log(getLastItem(favoriteThings));
console.log(getLastItem(voters));
