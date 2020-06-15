import requests
from flask import request
import datetime


class SpotifyClient:
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    access_token = None
    access_token_expires = None
    access_token_did_expire = True
    refresh_token = None

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_auth_url(self):
        """
        Get the Authorize URL for client
        """
        authorize_url = "https://accounts.spotify.com/authorize?"
        client_id = self.client_id
        redirect_uri = "http://localhost:5000/callback"
        scope = "user-read-private"
        query_params = f"client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
        request_auth = authorize_url + query_params
        return request_auth

    def get_auth_response(self):
        code = request.args.get("code")
        return code

    def auth_payload(self):
        access_token = self.access_token
        if access_token is None:
            code = self.get_auth_response()
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": "http://localhost:5000/callback",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }
            return data
        elif access_token is not None:
            refresh_token = self.refresh_token
            data = {
                "grant_type": "authorization_code",
                "code": refresh_token,
                "redirect_uri": "http://localhost:5000/callback",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }
            return data

    def perform_auth(self):
        """
        Have application request refresh and access tokens
        """
        post_request = requests.post(self.token_url, data=self.auth_payload())
        if post_request.status_code not in range(200, 299):
            raise Exception("Could not authorize client")
        data = post_request.json()
        now = datetime.datetime.now()
        access_token = data["access_token"]
        expires_in = data["expires_in"]
        expires = now + datetime.timedelta(seconds=expires_in)
        refresh_token = data["refresh_token"]
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        self.refresh_token = refresh_token
        return True

    def get_access_token(self):
        """
        Checks if tokens present, otherwise obtains them.
        """
        token = self.access_token
        expired = self.access_token_did_expire
        if expired:
            self.perform_auth()
            return self.get_access_token()
        elif token is None:
            self.perform_auth()
            return self.get_access_token()
        return token

class SpotifyGrab(SpotifyClient):
    access_token = SpotifyClient.access_token

    def __init__(self,*args, **kwargs):
        super(SpotifyGrab, self).__init__(*args, **kwargs)

    def get_user_profile(self):
        pass