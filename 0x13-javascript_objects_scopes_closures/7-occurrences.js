#!/usr/bin/node
/*
Empty class Rectangle that defines a rectangle
*/
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let element;
  for (element of list) {
    if (element === searchElement) {
      counter++;
    }
  }
  return (counter);
};
