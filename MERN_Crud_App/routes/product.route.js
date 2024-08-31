const express = require("express");
const router = express.Router();
const {
  getProducts,
  getProductById,
  updateProduct,
  createProduct,
  deleteProduct,
} = require("../controllers/product.controler.js");

router.get("/", getProducts);
router.get("/:id", getProductById);

router.put("/:id", updateProduct);

router.post("/", createProduct);

router.delete("/:id", deleteProduct);

module.exports = router;
