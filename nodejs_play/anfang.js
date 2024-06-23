#!/usr/bin/node

const http = require("http");

const server = http.createServer((req, res) => {
  console.log(req.url);
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ data: "Booyah!!" }));
});

server.listen(5000);
