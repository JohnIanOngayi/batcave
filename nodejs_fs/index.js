import { appendFile, readFile, rename, writeFile } from "fs";
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

        /* Renaming file asynchronously */
        rename(
          path.join(__dirname, "files", "reply.txt"),
          path.join(__dirname, "files", "__reply.txt"),
          (err) => {
            if (err) throw err;
            console.log("Rename complete!");
          },
        );
      },
    );
  },
);

process.on("uncaughtException", (error) => {
  console.error(error);
  process.exit(1);
});
