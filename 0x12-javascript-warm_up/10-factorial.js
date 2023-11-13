#!/usr/bin/node
/*
Prints factorial number
*/
function factorial (a) {
  let fact = a;
  if (isNaN(a) || a === 1) {
    return (1);
  }
  fact = fact * factorial(fact - 1);
  return fact;
}
const result = factorial(parseInt(process.argv[2]));
console.log(result);
