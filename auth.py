from mastodon import Mastodon
import config


def authenticate_mastodon():
    client_key = config.CLIENT_KEY
    client_secret = config.CLIENT_SECRET
    access_token = config.ACCESS_TOKEN
    api_base_url = "mastodon.social"

    mastodon = Mastodon(
        client_id=client_key,
        client_secret=client_secret,
        access_token=access_token,
        api_base_url=api_base_url
    )
    return mastodon
