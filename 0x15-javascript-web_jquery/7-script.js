#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER
*/
const $char = $('#character');
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (char) {
    $char.append(char.name);
  }
});
