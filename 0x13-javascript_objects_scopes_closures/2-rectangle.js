#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // no-empty
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
