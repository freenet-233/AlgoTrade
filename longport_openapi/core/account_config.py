# longport账户
import os

from dotenv import load_dotenv
from longport.openapi import Config


class AccountConfig:
    load_dotenv()
    appKey = os.getenv("LONGPORT_APP_KEY")
    appSecret = os.getenv("LONGPORT_APP_SECRET")
    accessToken = os.getenv("LONGPORT_ACCESS_TOKEN")
    accountConfig = Config(
        app_key=appKey,
        app_secret=appSecret,
        access_token=accessToken
    )
