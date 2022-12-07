from pytube import YouTube
#from moviepy.editor import *
import os

#下載影片並命名為tmp.mp4
def ytdown():
    url = input("輸入網址:")
    target_path = r"D:\downloads"
    file_name = input("輸入歌名:")

    #現已可以直接下載.mp3
    #YouTube(url).streams.first().download(
    YouTube(url).streams.filter(only_audio=True).first().download(
        filename = file_name+'.mp3',
        output_path = target_path
    )

ytdown()

"""
#將下載的mp4轉為mp3
def mp4_to_mp3(file_name):
    video = VideoFileClip(file_name)
    #檔名要加上.mp3
    music_name = input("輸入檔名:")
    video.audio.write_audiofile(music_name)
"""

"""
#讀取下載的mp4的檔案名稱
f_name = os.path.split('./tmp.mp4')
"""
#mp4_to_mp3(f_name[1])



