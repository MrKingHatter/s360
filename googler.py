!pip install gspread --upgrade

from google.colab import auth
import gspread
from oauth2client.client import GoogleCredentials


class Auth:
    def __init__(self):
        auth.authenticate_user()
        self.credentials = GoogleCredentials.get_application_default()
        self.client = None

    def authenticate(self) -> gspread.client.Client:
        self.client = gspread.authorize(self.credentials)
        return self.client

    def re_authenticate(self):
        if self.credentials.access_token_expired:
            self.client.login()  # refreshes the token
