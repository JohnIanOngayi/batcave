#!/usr/bin/node

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) resolve({ status: true, body: "success" });
    else reject(new Error("getFullResponseFromAPI(success)"));
  });
}
