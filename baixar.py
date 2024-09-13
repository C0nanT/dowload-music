import os

playlist_url = "https://www.youtube.com/watch?v=SRXH9AbT280&list=PLYbeiETwelFsYedOL9l_S9U5BQWyjxvIU&ab_channel=LinkinPark"

command = f'yt-dlp -i -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" -x --audio-format mp3 "{playlist_url}"'

os.system(command)

print("Download concluído!")
