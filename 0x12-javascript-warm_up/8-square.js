#!/usr/bin/node
/*
Print messages
*/
const size = parseInt(process.argv[2]);
let j;

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (j = 0; j < size; j++) {
    console.log('X'.repeat(size));
  }
}
