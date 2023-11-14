#!/usr/bin/node
/*
class Rectangle a rectangle
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // Prints the rectangle  X

  print () {
    let vtcal;
    for (vtcal = 0; vtcal < this.height; vtcal++) {
      console.log('X'.repeat(this.width));
    }
  }
};
