import pytube
url="https://www.youtube.com/watch?v=7BXJIjfJCsA"
yt=pytube.YouTube(url)
print(yt.thumbnail_url)
viedo=yt.streams.get_highest_resolution()
viedo.download('')