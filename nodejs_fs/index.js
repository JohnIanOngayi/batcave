import { readFile } from "fs";

/* Reading file asynchronously */
readFile("./files/starter.txt", 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data)
});

process.on("uncaughtException", (error) => {
  console.error(error);
  process.exit(1);
});
