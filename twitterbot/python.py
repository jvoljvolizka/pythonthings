import spotipy
import spotipy.util as ut 



export SPOTIPY_CLIENT_ID = '42cf8e4c8a994495b1823eef3de8049a'
export SPOTIPY_CLIENT_SECRET = 'ebdd218361fd4e0a8120607f060d5676'
export SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

user = "damnedprotoss"

#spotify:user:damnedprotoss:playlist:3D9dkvrm1lp7aIesZMSIXX

scope = "playlist-read-private"


def create_playlist_file (username,scopename):
	token = ut.prompt_for_user_token(username, scopename)
	print(token)


create_playlist_file(user,scope)