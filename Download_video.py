from __future__ import unicode_literals
import youtube_dl
f = open("banner.txt", "r")
print(f.read()) 
print("Coded by Sibin Thomas")
url = raw_input("Please enter your video url here>>")
urlstring = str(url)
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([urlstring])
print("--------------------------------------------")
