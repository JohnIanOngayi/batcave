const Product = require("../models/product.model.js");

// GET: Fetch all products
const getProducts = async (req, res) => {
  try {
    const products = await Product.find();
    res.status(200).json(products);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// GET: single product by id
const getProductById = async (req, res) => {
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
};

// PUT: update a product
const updateProduct = async (req, res) => {
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
};

// POST: create a product
const createProduct = async (req, res) => {
  try {
    const product = await Product.create(req.body);
    res.status(201).json(product);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// DELETE: delete a product
const deleteProduct = async (req, res) => {
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
};

module.exports = {
  getProducts,
  getProductById,
  updateProduct,
  createProduct,
  deleteProduct,
};
