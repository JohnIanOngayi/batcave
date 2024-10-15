import { appendFile, readFile, writeFile } from "fs";
import { fileURLToPath } from "url";
import path, { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/* Reading file asynchronously */
readFile(path.join(__dirname, "files", "starter.txt"), "utf-8", (err, data) => {
  if (err) throw err;
  console.log(data);
});

/* Writing to file asynchronously */
writeFile(
  path.join(__dirname, "files", "reply.txt"),
  "text data for reply.txt",
  (err) => {
    if (err) throw err;
    console.log("Write complete!");
    /* Appending to file asynchronously */
    appendFile(
      path.join(__dirname, "files", "reply.txt"),
      "text to append to reply.txt",
      (err) => {
        if (err) throw err;
        console.log("Append complete!");
      },
    );
  },
);

process.on("uncaughtException", (error) => {
  console.error(error);
  process.exit(1);
});
