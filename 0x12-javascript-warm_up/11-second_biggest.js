#!/usr/bin/node
/*
Prints the second higher int argument
*/
let ArgList = process.argv.slice(2);
if (ArgList.length > 1) {
  for (let i = 0; i < ArgList.length; i++) {
    ArgList[i] = parseInt(ArgList[i]);
  }
  ArgList = ArgList.sort();
  console.log(ArgList.slice(-2)[0]);
} else {
  console.log(0);
}
