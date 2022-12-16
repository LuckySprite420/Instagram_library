from pathlib import Path
from PIL import Image
from instagrapi import Client
from instagrapi.types import StoryMention, StoryLink, StoryHashtag, StoryMedia
from login import ACCOUNT_USERNAME, ACCOUNT_PASSWORD
import json
import time

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

warland = cl.user_info_by_username('warlandgame')

hashtag = cl.hashtag_info('playtoearn')

cl.photo_upload_to_story(
    'PHOTO_PATH', 
    "The new gaming platform",
    mentions=[StoryMention(user=warland, x=0.1, y=0.1, width=0.8333333333333334, height=0.125)],
    hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
)