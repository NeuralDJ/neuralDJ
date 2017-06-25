var DeeJay = (function(_access_token) { 
      var self = {};
      self.access_token = _access_token;
      self.spotify = new SpotifyWebApi();
      self.device_id = undefined;

      self.spotify.setAccessToken(self.access_token);

      //console.log('get my devices now maaan -- ' + _access_token);
      self.spotify.getMyDevices().then(function(data) {
        //console.log('getmydevice - success');
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
        self.spotify.skipToNext({ device_id: self.device_id }).then(function(data) {
            self.setCurrentTrack(500);
        });
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
            //console.log(data);
            self.skipSong();
        });
      }

      self.setCurrentTrack = function(delay)
      {
          if(delay === undefined || delay == null || delay < 0)
          {
              delay = 10
          }

          setTimeout(function() {
            //console.log('lets change songs!');
            var callback = self.spotify.getMyCurrentPlaybackState();
            callback.then(function(data) {
                //console.log(data.item.artists);
                $('#cTitle').text(data.item.name);
                $('#cArtist').text(data.item.artists[0].name);
                $('#cAlbum').text(data.item.album.name);
            });
          }, delay);

          
          //$('#cGenre').text('');

          //return callback;
      };
    
      return self;
  });
