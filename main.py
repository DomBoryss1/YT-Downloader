from pytube import YouTube
import os

def download_video(url, path, file_type):
    yt = YouTube(url)
    if file_type == "mp4":
        video = yt.streams.filter(file_extension='mp4').first()
    elif file_type == "mp3":
        video = yt.streams.filter(only_audio=True).first()
    else:
        print("Invalid file type. Please choose 'mp4' or 'mp3'.")
        return
    video.download(path)
    print(f'{file_type} downloaded successfully')

if __name__ == "__main__":
    url = input("Enter the YouTube video url: ")
    file_type = input("Enter the file type (mp4 or mp3): ")
    path = input("Enter the path to download the file: ")
    download_video(url, path, file_type)
