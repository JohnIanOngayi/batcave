#!/usr/bin/node
/*
 * Module defines a base class
 */
class Base {
  #nb_objects = 0;

  constructor(id) {
    if (id == null) {
      this.id = id;
    }
    this.#nb_objects += 1;
    this.id = this.#nb_objects;
  }
}

module.exports = Base;
