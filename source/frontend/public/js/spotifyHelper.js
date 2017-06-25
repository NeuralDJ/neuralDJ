var DeeJay = (function(_access_token) { 
      var self = {};
      self.access_token = _access_token;
      self.spotify = new SpotifyWebApi();
      self.device_id = undefined;

      self.spotify.setAccessToken(self.access_token);

      console.log('get my devices now maaan -- ' + _access_token);
      self.spotify.getMyDevices().then(function(data) {
        console.log('getmydevice - success');
        self.device_id = data.devices[0].id;
      });

      self.pause = function()
      {
        self.spotify.pause({ device_id: self.device_id });
      }

      self.play = function()
      {
        self.spotify.play({ device_id: self.device_id });
      }

      self.skipSong = function()
      {
        self.spotify.skipToNext({ device_id: self.device_id });
      }

      self.changeGenre = function(current_genre)
      {
        if(current_genre === undefined || current_genre === null)
        {
            current_genre = 'none';
        }

        return $.ajax({
          url: 'http://127.0.0.1:5002/api/genre/next/' + current_genre
        }).done(function(data) {
            console.log(data);
            self.skipSong();
        });
      }

      return self;
  });

$( document ).ready(function() {

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