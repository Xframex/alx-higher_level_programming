#!/usr/bin/node
/*
Read file content and print .
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
