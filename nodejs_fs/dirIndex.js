import { fileURLToPath } from "url";
import path, { dirname } from "path";
import { mkdir } from "fs/promises";
import { existsSync, rmdir } from "fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

try {
  if (!existsSync(path.join(__dirname, "new"))) {
    await mkdir(path.join(__dirname, "new"));
    console.log("New Directory Created");
  } else {
    // await rmdir(path.join(__dirname, "new"));
    console.log("Directory already exists");
  }
} catch (error) {
  throw error;
}

process.on("uncaughtException", (error) => {
  console.log(error);
  process.exit(1);
});
