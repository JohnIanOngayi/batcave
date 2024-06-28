#!/usr/bin/node

const fs = require("fs");
fs.readFile("./docs/text.txt", (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
console.log(`last line`);
const data = "Hell Yeahh!!";
fs.writeFile("./docs/write.md", data, () => {
  console.log(`Booyah!`);
});
