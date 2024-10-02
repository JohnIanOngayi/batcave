const express = require("express");
const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");

dotenv.config();

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const posts = [
  {
    username: "ian",
    title: "Node rules!",
  },
  {
    username: "John",
    title: "What a language!",
  },
];

const authenticateToken = (req, res, next) => {
  const authHeader = req.headers["authorization"];
  const access_token = authHeader.split(" ")[1];
  if (access_token == null) return res.sendStatus(401);
  jwt.verify(access_token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

app.get("/", (req, res) => {
  return res.json({ status: "OK" }).status(200);
});

app.get("/posts", authenticateToken, (req, res) => {
  return res.send(posts).status(200);
});

app.listen(8000, () => console.log(`Listening on port 8000`));
