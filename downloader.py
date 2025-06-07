from pytube import YouTube

def download(link):
    try:
        video = YouTube(link)
        video = video.streams.filter(file_extension="mp4").get_highest_resolution()
        video.download()
        print('Video downloaded successfully!')
    except:
        print('Download failed')
print('This program will download a YouTube video')


while True:
    link = input('Enter YouTube link to download (or Enter EXIT to quit) : ')
    if link.upper() == 'EXIT':
        print('Exiting program now...')
        break
    else:
        print('Downloading...')
        download(link)
