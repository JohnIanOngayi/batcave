#!/usr/bin/node

import { uploadPhoto, createUser } from "./utils";

export default async function asyncUploadUser() {
  let status = {};
  try {
    const photoStatus = await uploadPhoto();
    const userStatus = await createUser();
    status = {
      photo: photoStatus,
      user: userStatus,
    };
  } catch (err) {
    status = {
      photo: null,
      user: null,
    };
  }
  return status;
}
