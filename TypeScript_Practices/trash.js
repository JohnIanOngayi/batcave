#!/usr/bin/node
"use strict";
const scores = [10, 20, 30, 40, 50];
const favoriteThings = [
    "raindrops on roses",
    "whiskers on kittens",
    "bright copper kettles",
    "warm woolen mittens",
];
const voters = [
    { name: "Joe", age: 22 },
    { name: "Beth", age: 19 },
    { name: "Sam", age: 24 },
];
function getLastItem(array) {
    return array[array.length - 1];
}
console.log(getLastItem(scores));
console.log(getLastItem(favoriteThings));
console.log(getLastItem(voters));
