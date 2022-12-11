from instabot import Bot 
import time
import os 
import glob

try:
    user_name = str(input("Enter the targeted username:"))
    total_dms = int(input("Enter the number of DMs:"))
except Exception:
    print("Invalid input!")

os.system("rm -rf config")
my_bot = Bot() 

#login
my_bot.login(username="", password="")

followers_ids = my_bot.get_user_followers(user_name)

for count, each_follower in enumerate(followers_ids):
    if count > total_dms:
        break
    my_bot.follow(each_follower)
    time.sleep(5)
    username = my_bot.get_username_from_user_id(each_follower)
    message_text = "Hi! How are you? I'm sorry to bother, just wanted to let you know that we are hosting weekly poker tournmanets with free entries where you can win cash, NFTs, merch and much more: https://play.apeinpoker.com/?affiliate=warland . Besides that we also have an upcoming FREE MINT, and all you need is to get a WL spot. You can check all the info in our discord, i will leave a link. Thank you so much and have a great day! Maybe we will see each other at the table. https://discord.gg/EqBG3rW2Zx"
    my_bot.send_message(message_text, [username])
    time.sleep(20)
    