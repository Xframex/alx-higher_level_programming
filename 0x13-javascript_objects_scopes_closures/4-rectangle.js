#!/usr/bin/node
/*
class Rectangle that defines a rectangle
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // Prints the rectangle using the character X

  print () {
    let vtcal;
    for (vtcal = 0; vtcal < this.height; vtcal++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
  }
};
