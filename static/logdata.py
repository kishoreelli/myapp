from fyers_api import fyersModel
from fyers_api import accessToken
import webbrowser
import json

client_id = 'Z2XR14JKUA-100'
secret_key = 'L8F93X0TIS'
redirect_uri = 'http://localhost:8080/'
response_type = "code"
grant_type = "authorization_code"

session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key,
                                   redirect_uri=redirect_uri, response_type=response_type,
                                   grant_type=grant_type)


def firstlink(session=session):
    response = session.generate_authcode()
    print(response)
    webbrowser.open(response)
    return


def asscode(auth_code):
    session.set_token(auth_code)
    response = session.generate_token()
    access_token = response["access_token"]
    print("token=" + access_token)
    return access_token


access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDI3Mzk0MjgsImV4cCI6MTY0MjgxMTQyOCwibmJmIjoxNjQyNzM5NDI4LCJhdWQiOlsieDoyIiwiZDoyIiwiZDoxIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDZqYmt3dkl1Skhka2tkUDFNVDF0LXRKSW5Na0RHUnpjeU9aeVRqNzJqSnZkaGxLV1hDaEpCNmFoWlo2M2VSWVZqTDMyM25ubFZzWXVQOWtiZ3M1Wm0xb0ZrYWU5c2RJVmdrTzZDWW5zaUhONWp5ND0iLCJkaXNwbGF5X25hbWUiOiJFTExJICAgS0lTSE9SRSIsImZ5X2lkIjoiWEUwMDMzMyIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.dA8WxpHV4YnJcbCrvYXfTpZgW7FL8YFv8RwfrQHBG8I'

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,log_path="/home/Desktop/apiV2")

is_async = True
