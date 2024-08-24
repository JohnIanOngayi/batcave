#!/usr/bin/node
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const request = new XMLHttpRequest();
const URL = "https://jsonplaceholder.typicode.com/todos";

request.addEventListener("readystatechange", () => {
  // console.log(request, request.readyState);
  if (request.readyState === 4) {
    console.log(`${request.responseText}`);
  }
});

request.open("GET", `${URL}`);
request.send();
