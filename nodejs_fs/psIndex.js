import { readFile, writeFile, appendFile, rename } from "fs/promises";
import { fileURLToPath } from "url";
import path, { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

try {
  const data = await readFile(
    path.join(__dirname, "files", "starter.txt"),
    "utf-8",
  );
  console.log(data);

  await writeFile(
    path.join(__dirname, "files", "psReply.txt"),
    "Written by Promise\n",
  );
  console.log("Promise-Written Successfully!");

  await appendFile(
    path.join(__dirname, "files", "psReply.txt"),
    "Appended by Promise\n",
  );
  console.log("Promise-Appended Successfully!");

  await rename(
    path.join(__dirname, "files", "psReply.txt"),
    path.join(__dirname, "files", "__psReply.txt"),
  );
  console.log("Promise-Renamed Successfully!");
} catch (error) {
  throw error;
}

process.on("uncaughtException", (error) => {
  console.log(error);
  process.exit(1);
});
