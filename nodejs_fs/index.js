import { readFile } from "fs";

/* Reading file asynchronously */
readFile("./files/starter.txt", (err, data) => {
  if (err) throw err;
  console.log(data.toString("utf-8"));
});

process.on("uncaughtException", (error) => {
  console.error(error);
  process.exit(1);
});
