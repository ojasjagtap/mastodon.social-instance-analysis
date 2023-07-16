from mastodon import Mastodon
import pause
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


def save_users_to_file(filename):
    with open(filename, "w") as file:
        user_count = mastodon.instance_nodeinfo()['usage']['users']['total']
        iterations = user_count // 80
        for i in range(iterations + 1):
            if mastodon.ratelimit_remaining > 0:
                users = mastodon.directory(limit=80, offset=80 * i)
                for user in users:
                    file.write('%d\n' % user['id'])
            else:
                pause.until(mastodon.ratelimit_reset)


mastodon = authenticate_mastodon()
save_users_to_file("users.txt")
