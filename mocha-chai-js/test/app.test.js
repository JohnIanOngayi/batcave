import { assert } from "chai";
import { sayHello, addNums } from "../app.js";

describe("test_app", function () {
  it("sayHello should return hello", function () {
    assert.equal(sayHello(), "hello");
  });

  it("sayHello should return string type", function () {
    assert.typeOf(sayHello(), "string");
  });

  it("addNums should return sum of two nums", function () {
    assert.equal(addNums(1, 2), 3);
  });
});
