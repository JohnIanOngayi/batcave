#!/usr/bin/node

function getNum(num) {
  return new Promise((resolve, reject) => {
    if (num === 1) resolve("Booyahh!!");
    else reject("Nooooo");
  });
}

async function finisher() {
  const response = await getNum(1);
  console.log(response);
}

finisher(getNum(1));
