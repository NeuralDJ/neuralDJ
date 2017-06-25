$( document ).ready(function() {

    $('#updateSong').click(function() {
        console.log('requesting what is the nect genre...');
        
        getNextGenre().done(function(data) {
	        $('#cgenre').text(data);
        })

    });


    function obtainNewToken()
    {
        var url = '/refresh_token';
        
        var data = {
            'refresh_token': refresh_token
        };

        makeCall(url, data)
            .done(function(data) {
                access_token = data.access_token;
                oauthPlaceholder.innerHTML = oauthTemplate({
                    access_token: access_token,
                    refresh_token: refresh_token
                });
            });
    }

    function getNextGenre()
    {
        var url_getNext = 'http://127.0.0.1:5002/api/genre/next/current_genre_is_rock';

        return makeCall(url_getNext);
    }

    function makeCall(url, data)
    {
        return $.ajax({
          url: url,
          data: data
        })
    }
});