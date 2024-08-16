#!/usr/bin/node

/**
 * The amount of cash currently in the register.
 */
var cashInRegister: number = 100;

/**
 * The queue of orders.
 */
var orderQueue: OrderObj[] = [];

/**
 * The next pizza id.
 */
var nextPizzaId: number = 1;

/**
 * The next order id.
 */
var nextOrderId: number = 1;

/**
 * The menu containing available pizzas.
 */

/**
 * Represents a pizza object.
 */
type PizzaObj = {
  id: number;
  name: string;
  price: number;
};

/**
 * Represents an order object.
 */
type OrderObj = {
  pizza: PizzaObj;
  id: number;
  status: "ordered" | "completed";
};
var menu: PizzaObj[] = [
  { id: nextPizzaId++, name: "Margherita", price: 8 },
  { id: nextPizzaId++, name: "Pepperoni", price: 10 },
  { id: nextPizzaId++, name: "Hawaiian", price: 10 },
  { id: nextPizzaId++, name: "Veggie", price: 9 },
];

/**
 * Adds a new pizza to the menu.
 */
function addNewPizza(pizzaObj: Omit<PizzaObj, "id">): void {
  const newpizzaObj: PizzaObj = {
    id: nextPizzaId++,
    ...pizzaObj,
  };
  menu.push(newpizzaObj);
}

/**
 * Retrieves the details of a pizza from the menu based on the provided identifier.
 * The identifier can be either a string (pizza name) or a number (pizza id).
 *
 * @param {number | string} identifier - The identifier for the pizza, either its name or id.
 * @returns {object} - The pizza object from the menu.
 * @throws {Error} - Throws an error if the pizza is not found in the menu.
 */
function getPizzadetail(identifier: number | string): PizzaObj | never {
  if (typeof identifier === "string") {
    const pizza = menu.find(
      (value) => value.name.toLowerCase() === identifier.toLowerCase(),
    );
    if (!pizza) {
      throw new Error(`${identifier} isn't in today's menu`);
    }
    return pizza;
  } else if (typeof identifier === "number") {
    const pizza = menu.find((value) => value.id === identifier);
    if (!pizza) {
      throw new Error(`Pizza id: ${identifier} isn't in today's menu`);
    }
    return pizza;
  } else {
    throw new TypeError("Identifier must be a string or an id");
  }
}

/**
 * Places an order for a pizza.
 *
 * @param pizzaName The name of the pizza to order.
 * @returns The order object.
 */
function placeOrder(pizzaName: string): OrderObj | never {
  const pizza = menu.find(
    (value) => value.name.toLowerCase() === pizzaName.toLowerCase(),
  );
  if (!pizza) {
    throw new Error(`${pizzaName} isn't in today's menu`);
  }
  cashInRegister += pizza.price;
  const order: OrderObj = { pizza, id: nextOrderId, status: "ordered" };
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
function completeOrder(orderId: number): OrderObj | never {
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
// console.log(getPizzadetail("Margherita"));
// console.log(getPizzadetail(2));
//
// let order1 = placeOrder("Margherita");
// let order2 = placeOrder("Pepperoni");
// let order3 = placeOrder("Supreme");
// console.log(orderQueue);
//
// completeOrder(1);
// completeOrder(2);
// console.log(orderQueue);
//
// console.log(cashInRegister);
