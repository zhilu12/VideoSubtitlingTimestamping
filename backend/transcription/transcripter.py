import os 
import librosa
import numpy as np
import torch
import pandas as pd
import whisper
import torchaudio

from tqdm.notebook import tqdm

# pydub import
from pydub import AudioSegment




# Dir where samples are kept
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

samples_dir = os.path.join(root, "data", "samples")

# Librosa implementation
def librosa_load_file(file_name):
  audio_dir = os.join(samples_dir, file_name)
  audio_data, sampling_rate = librosa.load(os.join(audio_dir, "audio.m4a"))  # Can be other formats too
  print(f"Sampling Rate: {sampling_rate} Hz")
  print(f"Audio Data Shape: {audio_data.shape}")
  print(f"Data Type: {audio_data.dtype}")

# Pydub implementation
def pydub_load_file(file_name):
  audio = AudioSegment.from_file(os.join(samples_dir, file_name), format='m4a') # Specify format if needed
  audio_data = audio.get_array_of_samples()
  sampling_rate = audio.frame_rate
  print(f"Sampling Rate: {sampling_rate} Hz")
  print(f"Audio Data Length: {len(audio_data)}")
  print(f"Data Type: {audio_data.dtype}")






# Transcripting with openAI whisper




# Testing entrypoint and code

if __name__ == "__main__":
    file_name = ''
    
    file_data = # audio data loader
    
    output = # processed file_data with openAI whisper
    
    
    # Saves to samples/data/file_name
      # maybe a folder under samples/data/file_name for both the audio and transcript
    
    print("Downloaded to:", output)
