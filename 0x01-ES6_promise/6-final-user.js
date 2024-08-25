#!/usr/bin/node

import { signUpUser } from "./4-user-promise";
import { uploadPhoto } from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  const data = Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((values) => {
    values.map((value) => {
      if (value.status != "fulfilled") {
        return {
          status: "rejected",
          value: value.reason.toString(),
        };
      }
      return value;
    });
  });
  return Promise.resolve(data);
}
