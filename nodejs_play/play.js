#!/usr/bin/node

const fs = require("fs");

if (!fs.existsSync("./deletables")) {
  fs.mkdir("./deletables", () => {
    console.log("Created Folder");
  });

  if (!fs.existsSync("./deletables/delete_me")) {
    fs.writeFile("./deletables/delete_me", "Hey oh Dr!", () => {
      console.log("Created and Wrote into delete_me!");
    });
  } else {
    console.log("delete_me already exists, we finna delete it!");
    fs.unlink("./deletables/delete_me", (err) => {
      if (err) {
        console.log(`ERROR WHILE DELETING delete_me`);
        console.log(err);
      } else {
        console.log("Successfully Deleted delete_me");
      }
    });
  }
} else {
  fs.rmdir("./deletables/", (err) => {
    if (err) {
      console.log(`ERROR WHILE DELETING FOLDER!`);
      console.log(err);
    } else {
      console.log("Successfully Deleted deletables folder");
    }
  });
}
