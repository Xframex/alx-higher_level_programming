#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER
*/
const $films = $('#list_movies');
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const filmList = data.results;
  for (const film of filmList) {
    $films.append('<li>' + film.title + '</li>');
  }
});
