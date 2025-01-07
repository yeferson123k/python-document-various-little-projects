"""
Instaloader is a tool to download pictures (or videos) along
with their captions and other metadata from Instagram.

you need install that library for import it
"""
import instaloader

def profile():
	obj = instaloader.Instaloader()
	username = input("Enter the username: ")
	obj.download_profile(username, profile_pic_only=True)
	return 

profile()
