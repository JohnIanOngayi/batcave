const express = require("express");
const productRoute = express.Router();
const Product = require("../models/product.model.js");
const {
  getProducts,
  getProductById,
  createProduct,
  updateProduct,
  deleteProduct,
} = require("../controllers/product.controllers.js");

productRoute.get("/", getProducts);

productRoute.get("/:id", getProductById);

productRoute.post("/", createProduct);

productRoute.put("/:id", updateProduct);

productRoute.delete("/:id", deleteProduct);

module.exports = productRoute;
