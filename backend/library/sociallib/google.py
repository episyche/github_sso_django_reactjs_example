from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the user info
        """
        auth_token1 = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwMmYzMDViNzA1ODEzMjlmZjI4OWI1YjNhNjcyODM4MDZlY2E4OTMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NjE4NTkwNjIsImF1ZCI6Ijg4Njg1NDMwMjEyNi0wOWcwcjhscTUzNXRocXBlYmJoMTNiYWpncnMxcWdqai5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwMjk4NDkyNzIxMzkzNjg4MDIyMCIsImVtYWlsIjoia2FydmVudGhhbmFpdEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiODg2ODU0MzAyMTI2LTA5ZzByOGxxNTM1dGhxcGViYmgxM2JhamdyczFxZ2pqLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6ImthcnZlbnRoYW4gSyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BSXRidm1uQzRuZUpLQmlQc1hKcUlsX3cwY0RXWUZWZU5qeUFWS0xEOWdjdT1zOTYtYyIsImdpdmVuX25hbWUiOiJrYXJ2ZW50aGFuIiwiZmFtaWx5X25hbWUiOiJLIiwiaWF0IjoxNjYxODU5MzYyLCJleHAiOjE2NjE4NjI5NjIsImp0aSI6IjAzMWQ4YjhiMGYxNzUyOGY2OWZmNDgzMzk2ZDg2NGI3OGJjN2ZjOTUifQ.Sh62A1DkrJVc6En03MIgqD-usDogmfVx4TzjAHJBRWHi0BsKhc8lL5Nqo2-EXcnrqPg2WLkp6ZVFcUrB-EkUEaD3B_tCHq7bShdP8WcJh2gtQ4EbmsBSHHKqISShKHyJ1ofmpksVIFC5gTEJWJ33BAPWv4AopOq6gjUG1KWx58Qzb4uGZHKhquQZBA1_YCOB35eAaJLHHiN_kcfW4l05G-aNbpHEc68bjIuCqFJ2gZ_8-pH_on63Iu6Kg2XYB7vMFda6WD0AQxJ-k_qEseCdg8vNhQp9WRgfszQAscDz7qqEiOIJaWDDXTxR1SPfuUqBrmTJ1S8sAsbqCEKvhePf4w"
        try:
            idinfo = id_token.verify_oauth2_token(
                
                auth_token1, requests.Request())
            if 'accounts.google.com' in idinfo['iss']:
                return idinfo

        except:
            return "The token is either invalid or has expired"