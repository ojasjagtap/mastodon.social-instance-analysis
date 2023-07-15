from auth import authenticate_mastodon
import pause


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
