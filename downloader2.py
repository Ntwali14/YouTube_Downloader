from pytube import YouTube
import sys

def download_video(url):
    try:
        # Clean the URL by removing any parameters and fixing Shorts URL
        if 'shorts' in url:
            video_id = url.split('/shorts/')[1].split('?')[0]
            url = f'https://www.youtube.com/watch?v={video_id}'
        else:
            url = url.split('?')[0]  # Remove any query parameters

        yt = YouTube(
            url,
            use_oauth=True,
            allow_oauth_cache=True
        )
        
        # Print video info
        print(f'\nVideo Info:')
        print(f'Title: {yt.title}')
        print(f'Author: {yt.author}')
        print(f'Length: {yt.length} seconds')
        print(f'Views: {yt.views}')
        
        # Print available streams (optional)
        print('\nAvailable streams:')
        for stream in yt.streams:
            print(stream)

        # Download the highest resolution stream
        print('\nDownloading...')
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f'Download completed successfully to current directory!')
        print(f'Filename: {yt.title}.mp4')

    except Exception as e:
        print(f'\nError: {e}')
        print('Possible solutions:')
        print('- Try again with a different URL')
        print('- Update pytube: pip install --upgrade pytube')
        print('- Try using yt-dlp instead (pip install yt-dlp)')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python downloader.py <YouTube URL>')
        print('Example: python downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    else:
        url = sys.argv[1]
        download_video(url)