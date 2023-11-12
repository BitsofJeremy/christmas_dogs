# toot_it_out.py
import argparse
import os
import sys
from mastodon import Mastodon

# Example
#
# python toot_it.py --send "Test from Python"
#
# Get you access token and instance from .env
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
MASTODON_INSTANCE = os.getenv('MASTODON_INSTANCE')

# Initialize
mastodon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url=MASTODON_INSTANCE
)


def send_toot(status, in_reply_to_id=None, media_ids=None):
    """ Just sends text to Mastodon """
    res = mastodon.status_post(
        status=status,
        in_reply_to_id=in_reply_to_id,
        media_ids=media_ids
    )
    if res:
        # print(f'toot sent!')
        return res
    else:
        # print(f'doh: {res}')
        return False


def send_media(media_file, description):
    """ Uploads Media to Mastodon """
    res = mastodon.media_post(media_file, description)
    if res:
        # print(f'toot sent!')
        return res
    else:
        # print(f'doh: {res}')
        return False


def main(**kwargs):
    if kwargs.get('send'):
        send_toot(status=kwargs.get('send'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--send',
        help='Send Tweet',
        required=True
    )

    args = parser.parse_args()

    # Convert the argparse.Namespace to a dictionary: vars(args)
    arg_dict = vars(args)
    # pass dictionary to main
    main(**arg_dict)
    sys.exit(0)
