$(function () {
  const Hello = $('#character');

  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $(data.hello).appendTo(Hello);
    }
  });
});
