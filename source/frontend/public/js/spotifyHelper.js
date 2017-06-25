$( document ).ready(function() {

    $('#updateSong').click(function() {
        console.log('#someButton was clicked');

        console.log(getNextGenre());
	    $('#csong').text("TEST");
    });


    function obtainNewToken()
    {
        $.ajax({
          url: '/refresh_token',
          data: {
            'refresh_token': refresh_token
          }
        }).done(function(data) {
          access_token = data.access_token;
          oauthPlaceholder.innerHTML = oauthTemplate({
            access_token: access_token,
            refresh_token: refresh_token
          });
        });
    }

    function getNextGenre()
    {
        makeCall('http://127.0.0.1:5002/api/genre/next/current_genre_is_rock').done(function(data) {

            console.log("next genre: ");
            console.log(data);
            return 'classical';
        });
    }

    function makeCall(url, data)
    {
        return $.ajax({
          url: url,
          data: data
        })
    }
});