import random
from instagrapi import Client

# with open("credential.txt","r") as f:
#     username,password = f.read().splitlines

username = "#########"
password = "$$$$$$$"

client = Client()
client.login(username,password)

hashtag = "programming"
comments = ["Awesome","Great","Nice"]

medias = client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i+1} of hashtag {hashtag}")  
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username}")
        comment = random.choice(comments)
        client.media_comment(media.id,comment)
        
        print(f"Commented {comment} under post number {i+1}")