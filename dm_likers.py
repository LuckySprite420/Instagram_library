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

liker_ids = my_bot.get_user_likers(user_name)

for count, each_liker in enumerate(liker_ids):
    if count > total_dms:
        break
    my_bot.follow(each_liker)
    time.sleep(5)
    username = my_bot.get_username_from_user_id(each_liker)
    message_text = ""
    my_bot.send_message(message_text, [username])
    time.sleep(20)
    