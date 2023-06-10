(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const movies = data.results;
      const list = $('#list_movies');
      $.each(movies, function (index, movie) {
        const title = movie.title;
        list.append('<li>' + title + '</li>');
      });
    }
  });
});
