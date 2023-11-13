#!/usr/bin/node
/*
Print messages
*/
const num = parseInt(process.argv[2]);
if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
