from google.colab import auth
import gspread
from oauth2client.client import GoogleCredentials


class Auth:
    def __init(self):
        self.credentials = GoogleCredentials.get_application_default()
        self.client = None
        
    def authenticate(self) -> gspread.client.Client:
        auth.authenticate_user()
        client = gspread.authorize(GoogleCredentials.get_application_default())
        return client

    def re_authenticate() -> gspread.client.Client:
        if self.credentials.access_token_expired:
            client.login()  # refreshes the token
