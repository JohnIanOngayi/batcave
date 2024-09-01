const express = require("express");
const mongoose = require("mongoose");
const productRoute = require("./routes/product.route");
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/api/products", productRoute);

app.get("/", (req, res) => {
  res.send("Tony Soprano says hello");
});

mongoose.connect("mongodb://127.0.0.1:27017/my_crud_api").then(() => {
  console.log("Database successfully conected");
  app.listen(3000, () => {
    console.log("Listening on port 3000");
  });
});
