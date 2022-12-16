import random
from instagrapi import Client
from login import ACCOUNT_USERNAME, ACCOUNT_PASSWORD
import time

client = Client()
client.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

hashtag = "INSERT_HASHTAG"
count = 0
while count <= 10:
    comments = ["Cool art!","Love it!", "LFG!", "Amazing!", "Killer art!", "Now that's something cool!", "Unique!", "Best thing that i saw today!", "Dope!", "AWESOME!", "Nice one!"]
    comment = random.choice(comments)
    try:
        count +=1  
        medias = client.hashtag_medias_recent(hashtag, 10)

        for i, media in enumerate(medias):
            client.media_like(media.id)
            print(f"Liked post number {i+1} of hashtag {hashtag}")
            time.sleep(5)
            if i % 5 == 0:
                client.user_follow(media.user.pk)
                print(f"Followed user {media.user.username}")
                time.sleep(5)
                client.media_comment(media.id, comment)
                print(f"Commented {comment} under post number {i+1}")
                time.sleep(2)
        if count==10:
            break
    except:
        pass