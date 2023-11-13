#!/usr/bin/node
/*
Print messages
*/
const x = parseInt(process.argv[2]);
let i = 0;

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (; i < x; i++) {
    console.log('C is fun');
  }
}
