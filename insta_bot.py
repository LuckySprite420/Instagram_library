from instabot import Bot 
import time
import os 
import glob

os.system("rm -rf config")
my_bot = Bot() 

#login
my_bot.login(username="", password="")

#comment
media_id = my_bot.get_hashtag_medias("nft")
my_bot.comment_hashtag('nft', amount=150)
time.sleep(5)

my_bot.unfollow_non_followers()

#like a post
my_bot.like_hashtag("nft", amount=200)
time.sleep(5)

my_bot.logout()
