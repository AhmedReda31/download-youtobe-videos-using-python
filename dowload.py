from pytube import YouTube

link= ("https://youtu.be/0oKPHmdF3Vs")

yt = YouTube(link)

yt.streams.first().download()

