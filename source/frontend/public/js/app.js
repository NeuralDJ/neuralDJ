$( document ).ready(function() {

  var access_token = undefined;
  var refresh_token = undefined;
  var error = undefined;

  function init() {
    /**
     * Obtains parameters from the hash of the URL
     * @return Object
     */
    function getHashParams() {
      var hashParams = {};
      var e, r = /([^&;=]+)=?([^&;]*)/g,
          q = window.location.hash.substring(1);
      while ( e = r.exec(q)) {
         hashParams[e[1]] = decodeURIComponent(e[2]);
      }
      return hashParams;
    }

    var userProfileSource = document.getElementById('user-profile-template').innerHTML,
        userProfileTemplate = Handlebars.compile(userProfileSource),
        userProfilePlaceholder = document.getElementById('user-profile');
    var oauthSource = document.getElementById('oauth-template').innerHTML,
        oauthTemplate = Handlebars.compile(oauthSource),
        oauthPlaceholder = document.getElementById('oauth');
    var params = getHashParams();

    access_token = params.access_token;
    refresh_token = params.refresh_token;
    error = params.error;

    if (error) {
      alert('There was an error during the authentication');
    } else {
      if (access_token) {
        // render oauth info
        oauthPlaceholder.innerHTML = oauthTemplate({
          access_token: access_token,
          refresh_token: refresh_token
        });
        $.ajax({
            url: 'https://api.spotify.com/v1/me',
            headers: {
              'Authorization': 'Bearer ' + access_token
            },
            success: function(response) {
              userProfilePlaceholder.innerHTML = userProfileTemplate(response);
              $('#login').hide();
              $('#loggedin').show();
            }
        });
      } else {
          // render initial screen
          $('#login').show();
          $('#loggedin').hide();
      }
    }

    if(access_token)
    {
      run();
    }  
  }
  


  
  function run()
  {
    var dj = new DeeJay(access_token);
    dj.setCurrentTrack();

    $('#playBtn').click(function() {
      //console.log('play song');
      dj.play();
    });
  
    $('#pauseBtn').click(function() {
      //console.log('play song');
      dj.pause();
    });

    $('#nextBtn').click(function() {
      //console.log('next song');
      dj.skipSong();
    });

    $('#analyzeRoomBtn').click(function() {
      //console.log('analyze room');
      dj.changeGenre();
    });

    $('#updateSong').click(function() {
      //console.log('getting current song');
      dj.setCurrentTrack();
    });
  }

  init();
});