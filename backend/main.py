from utils.utils import download_audio
from transcription.transcripter import transcribe_by_title
import os 

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
samples_dir = os.path.join(root, "data", "samples")

if __name__ == "__main__":
    url = "https://www.twitch.tv/videos/2434034103"

    folder_name = download_audio(url, samples_dir)
    results = transcribe_by_title(folder_name, samples_dir)

    # Optional: save results to text file
    output_path = os.path.join(samples_dir, folder_name, "transcript.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        for chunk_id, text in results:
            f.write(f"[Chunk {chunk_id}]\n{text}\n\n")

    print(f"\nTranscript saved to: {output_path}")
