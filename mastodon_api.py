from mastodon import Mastodon

def api():
    return Mastodon(access_token='.token.secret',api_base_url='https://mastodon.world/')
