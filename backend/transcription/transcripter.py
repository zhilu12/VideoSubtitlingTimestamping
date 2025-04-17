import os
from pydub import AudioSegment
import numpy as np
import torch
import whisper

def load_audio_chunks(file_path, chunk_length_ms=60 * 1000):
    audio = AudioSegment.from_file(file_path)
    chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def audiosegment_to_tensor(audio_segment):
    samples = np.array(audio_segment.get_array_of_samples()).astype(np.float32)
    samples /= np.iinfo(audio_segment.array_type).max  # Normalize to [-1, 1]
    return torch.from_numpy(samples)

def transcribe_chunks(chunks, model_name="base"):
    model = whisper.load_model(model_name)
    results = []

    for i, chunk in enumerate(chunks):
        tensor = audiosegment_to_tensor(chunk)
        audio = whisper.pad_or_trim(tensor)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        result = model.decode(mel, whisper.DecodingOptions())
        print(f"[Chunk {i}] {result.text}")
        results.append((i, result.text))

    return results

# Getting audio file from folder
def find_audio_file(folder_path, extensions=('m4a', 'mp4', 'mp3', 'wav', 'aac')):
    for ext in extensions:
        candidate = os.path.join(folder_path, f"audio.{ext}")
        if os.path.exists(candidate):
            return candidate
    raise FileNotFoundError("No supported audio file found in folder")

def transcribe_by_title(folder_name, samples_dir):
    folder_path = os.path.join(samples_dir, folder_name)
    file_path = find_audio_file(folder_path)
    chunks = load_audio_chunks(file_path)
    return transcribe_chunks(chunks)