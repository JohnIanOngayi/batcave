const express = require("express");
const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");

dotenv.config();

const app = express();
app.use(express.json());

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

const generateAccessToken = (user) => {
  return jwt.sign(user, process.env.ACCESS_TOKEN_SECRET, { expiresIn: "15s" });
};

const generateRefreshToken = (user) => {
  return jwt.sign(user, process.env.REFRESH_TOKEN_SECRET);
};

app.post("/login", (req, res) => {
  const username = req.body.username;
  const user = { username };
  const access_token = generateAccessToken(user);
  const refresh_token = generateRefreshToken(user);

  res.json({ access_token, refresh_token });
});

app.listen(8001, () => console.log(`Listening on port 8001`));
