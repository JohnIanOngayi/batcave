#!/usr/bin/node
"use strict";
let myName = "Bob";
let numberOfWheels = 4;
let isStudent = false;
/**
 * The menu containing available pizzas.
 */
const menu = [
    { name: "Margherita", price: 8 },
    { name: "Pepperoni", price: 10 },
    { name: "Hawaiian", price: 10 },
    { name: "Veggie", price: 9 },
];
/**
 * The amount of cash currently in the register.
 */
let cashInRegister = 100;
/**
 * The queue of orders.
 */
const orderQueue = [];
/**
 * The next order id.
 */
let nextOrderId = 1;
/**
 * Adds a new pizza to the menu.
 */
function addNewPizza(pizzaObj) {
    menu.push(pizzaObj);
}
/**
 * Places an order for a pizza.
 *
 * @param pizzaName The name of the pizza to order.
 * @returns The order object.
 */
function placeOrder(pizzaName) {
    const pizza = menu.find((value) => value.name === pizzaName);
    if (!pizza) {
        throw new Error(`${pizzaName} isn't in today's menu`);
    }
    cashInRegister += pizza.price;
    const order = { pizza, status: "ordered", id: nextOrderId };
    orderQueue.push(order);
    nextOrderId += 1;
    return order;
}
/**
 * Completes an order.
 *
 * @param orderId The id of the order to complete.
 * @returns The completed order.
 */
function completeOrder(orderId) {
    const order = orderQueue.find((value) => value.id === orderId);
    if (!order) {
        throw new Error(`Order id:${orderId} doesn't exist in orderqueue`);
    }
    order.status = "completed";
    return order;
}
console.log(menu);
addNewPizza({ name: "BBQ Chicken", price: 12 });
addNewPizza({ name: "Meat Lovers", price: 12 });
addNewPizza({ name: "Supreme", price: 12 });
console.log(menu);
let order1 = placeOrder("Margherita");
let order2 = placeOrder("Pepperoni");
let order3 = placeOrder("Supreme");
console.log(orderQueue);
completeOrder(1);
completeOrder(2);
console.log(orderQueue);
console.log(cashInRegister);
