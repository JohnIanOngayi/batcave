const express = require("express");
const mongoose = require("mongoose");
const app = express();
const Product = require("./models/product.model.js");

// Added middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.send("Tony Soprano says hello and goodbye");
});

app.get("/api/products", async (req, res) => {
  try {
    const products = await Product.find();
    res.status(200).json(products);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.get("/api/products/:id", async (req, res) => {
  try {
    const { id } = req.params;
    // const product = await Product.findById(id);
    const query = Product.findOne({ _id: id });
    query.getFilter();
    const product = await query.exec();
    res.status(200).json(product);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.put("/api/products/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const product = await Product.findByIdAndUpdate(id, req.body);
    if (!product) {
      return res.status((404).json({ message: `Product doesn't exist` }));
    }
    const updatedProduct = await Product.findById(id);
    res.status(200).json(updatedProduct);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.post("/api/products", async (req, res) => {
  try {
    const product = await Product.create(req.body);
    res.status(201).json(product);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

app.delete("/api/products/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const product = await Product.findById(id);
    if (!product) {
      return res.status((404).json({ message: `Product doesn't exist` }));
    }
    const resp = await Product.findByIdAndDelete(id);
    res.status(200).json({ message: resp.deletedCount });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

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
