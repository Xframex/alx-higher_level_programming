#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER
*/
$('#toggle_header').click(function () {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
