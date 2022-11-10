from app.utils.security.oauth.impl.google import google


def provide_oauth(oauth_type: str):
    return {
        'google': google
    }[oauth_type]
