import { readFile } from "fs";
import { fileURLToPath } from "url";
import path, { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/* Reading file asynchronously */
readFile(path.join(__dirname, "files", "starter.txt"), "utf-8", (err, data) => {
  if (err) throw err;
  console.log(data);
});

process.on("uncaughtException", (error) => {
  console.error(error);
  process.exit(1);
});
