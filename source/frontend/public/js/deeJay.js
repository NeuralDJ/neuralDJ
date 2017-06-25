var DeeJay = (function(_access_token) { 
      var self = {};
      self.access_token = _access_token;
      self.spotify = new SpotifyWebApi();
      self.device_id = undefined;

      self.spotify.setAccessToken(self.access_token);

      //console.log('get my devices now maaan -- ' + _access_token);
      self.spotify.getMyDevices().then(function(data) {
        //console.log(data);
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

      self.changeGenre = function(request_type, current_genre)
      {
        if(current_genre === undefined || current_genre === null)
        {
            current_genre = 'none';
        }

        if(request_type === undefined || request_type === null)
        {
            //features
            //emotion
            request_type = 'emotion';
        }


        return $.ajax({
          url: 'http://127.0.0.1:5002/api/genre/next/' + request_type + '/' + current_genre
        }).done(function(data) {
            console.log(data);
            self.skipSong();
        });
      }

      self.setRoomSettings = function()
      {
        console.log('set room info');

        // hide content
        $('#container_room > #content').hide();
        // show loading
        $('#container_room > #loading').show();
        return $.ajax({
          url: 'http://127.0.0.1:5002/api/genre/next/features/none'
        }).done(function(data) {
            console.log('returned info');
            console.log(data);
            var root = '#container_room > #content > #info > '; 
            $(root + '#age > span').text(data['age']);
            $(root + '#gender > span').text(data['gender']);
            $(root + '#scene > span').text(data['scene'].join(", "));

            // hide content
            $('#container_room > #loading').hide();
            // show loading
            $('#container_room > #content').show();
        });
      }

      self.setEmotions = function()
      {
                // hide content
        $('#container_emotion > #content').hide();
        // show loading
        $('#container_emotion > #loading').show();

          console.log('set emotion info');
          return $.ajax({
            url: 'http://127.0.0.1:5002/api/genre/next/emotion/rock'
          }).done(function(data) {
            console.log('returned info');
            console.log(data);
            var root = '#container_emotion > #content > #info > '; 
            $(root + '#changeSong > span').text(data['changeSong']);
            $(root + '#emotion > span').text(data['emotion']);

            if(data['changeSong'] === 'yes')
            {
              self.skipSong();
            }

            // hide content
            $('#container_emotion > #loading').hide();
            // show loading
            $('#container_emotion > #content').show();
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
                console.log(data);

                if(data.item !== null)
                {
                  $('#cTitle').text(data.item.name);
                  $('#cArtist').text(data.item.artists[0].name);
                  $('#cAlbum').text(data.item.album.name);
                }
            });
          }, delay);

          
          //$('#cGenre').text('');

          //return callback;
      };
    
      return self;
  });
