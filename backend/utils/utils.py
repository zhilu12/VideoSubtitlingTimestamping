# handles getting audio file from link
import os
import yt_dlp

# Returns video title given url
def get_video_title(url):
    ydl_opts = {
        'quiet': True, 
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as  ydl:
        info = ydl.extract_info(url, download=False)
        return info['title']

# Cleans up video title for folder name
def sanitize_title(title):
    return "".join(c for c in title if c.isalnum() or c in (' ', '_', '-')).rstrip()

# Downloads the audio file given url
def download_audio(url, samples_dir):
    title = sanitize_title(get_video_title(url))
    output_dir = os.path.join(samples_dir, title)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "audio.%(ext)s")


    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'concurrent_fragment_download': 5,
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return title


# test entrypoint
if __name__ == "__main__":
    test_url = "https://www.twitch.tv/videos/2434034103"
    output = download_audio(test_url)
    print("Downloaded to:", output)
