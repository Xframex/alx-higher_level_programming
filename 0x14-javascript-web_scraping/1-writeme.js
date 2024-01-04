#!/usr/bin/node
/*
Writes content of a file.
*/
const fs = require('fs');
// Rewriting the arv 
const argv = process.argv.slice(2);
fs.writeFile(argv[0], argv[1], 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
