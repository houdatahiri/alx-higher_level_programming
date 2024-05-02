// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      let films = data.results;
      for (let i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
