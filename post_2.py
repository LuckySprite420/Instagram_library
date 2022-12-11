from pathlib import Path
from PIL import Image
from instagrapi import Client
from login import ACCOUNT_USERNAME, ACCOUNT_PASSWORD
import json
import time

image = Image.open("")
image = image.convert("RGB")
new_image = image.resize((1080, 1080))
new_image.save("new_picture2.jpg")

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

phot_path = "new_picture2.jpg"
phot_path  = Path(phot_path)

cl.photo_upload(phot_path , "#NFT #Nftart #Nftartist #NFTcommunity #playtoearn #Metaverse #Solana #Giveaway #Poker #warland #Freemint")
