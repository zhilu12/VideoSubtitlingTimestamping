# handles getting audio file from link
import os
import yt_dlp

def download_audio(url):
    # Output path for audio file
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    samples_dir = os.path.join(root, "data", "samples")

    output_path = os.path.join(samples_dir, "%(title)s", "audio.%(ext)s")


    # Downloading audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'concurrent_fragment_download': 5,
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([url])

    return output_path


# test entrypoint
if __name__ == "__main__":
    test_url = "https://www.twitch.tv/videos/2434034103"
    output = download_audio(test_url)
    print("Downloaded to:", output)
