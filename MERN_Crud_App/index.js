const express = require("express");
const mongoose = require("mongoose");
const app = express();
const Product = require("./models/product.model.js");
const productRoute = require("./routes/product.route.js");

// Added middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.send("Welcome to my garage 🚘");
});

// routes
app.use("/api/products", productRoute);

mongoose
  .connect("mongodb://127.0.0.1:27017/MERN_crud_app")
  .then(() => {
    console.log("Successfully connected to db");

    app.listen((port = 3000), () => {
      console.log("Server is listening on port 3000");
    });
  })
  .catch(() => {
    console.error("db connection failed");
  });
