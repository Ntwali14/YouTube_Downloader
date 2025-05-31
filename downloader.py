from pytube import YouTube
import sys

def download_video(url):
    """
    Downloads a YouTube video given its URL with highest available resolution
    
    Args:
        url (str): The URL of the YouTube video to download
    """
    try:
        yt = YouTube(
    'https://www.youtube.com/watch?v=jT4SKemBZVM',
    use_oauth=True,
    allow_oauth_cache=True
)
        for stream in yt.streams:
            print(stream)
            
        # Display video information
        print(f'Title: {yt.title}')
        print(f'Author: {yt.author}')
        print(f'Length: {yt.length} seconds')
        print(f'Views: {yt.views}')
        print(f'Rating: {yt.rating}')
        print('Downloading...')

        # Get the highest resolution stream and download
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print('Download completed successfully!')
    except Exception as e:
        print('Error: ',e)

if __name__ == '__main__':
    # Check if URL is provided as command line argument
    if len(sys.argv) < 2:
        print('Usage: python downloader.py <YouTube URL>')
    else:
        url = sys.argv[1]
        download_video(url)