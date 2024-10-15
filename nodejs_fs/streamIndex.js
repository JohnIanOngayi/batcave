import { fileURLToPath } from "url";
import path, { dirname } from "path";
import { createReadStream, createWriteStream } from "fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

try {
  const rs = createReadStream(path.join(__dirname, "files", "lorem.txt"), {
    encoding: "utf-8",
  });
  const ws = createWriteStream(path.join(__dirname, "files", "newLorem.txt"));

  /** Streamz more efficient */
  rs.on("data", (dataChunk) => {
    console.log(`dataChunk from rs: \n${dataChunk}`);
    ws.write(dataChunk);
    console.log("Finished writing");
  });
} catch (error) {
  throw error;
}

process.on("uncaughtException", (error) => {
  console.log(error);
  process.exit(1);
});
