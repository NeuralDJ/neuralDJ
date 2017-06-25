$( document ).ready(function() {

    $('#updateSong').click(function() {
        console.log('#someButton was clicked');
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

});