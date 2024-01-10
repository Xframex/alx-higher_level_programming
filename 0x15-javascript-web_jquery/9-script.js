#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER
*/
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('#hello').text(data.hello);
});
