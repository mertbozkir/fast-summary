import torch
from faster_whisper import WhisperModel
from datasets import load_dataset

# define our torch configuration
device = "cuda:0" if torch.cuda.is_available() else "cpu"
compute_type = "float16" if torch.cuda.is_available() else "float32"

# load model on GPU if available, else cpu
model = WhisperModel("distil-large-v3", device=device, compute_type=compute_type)

# load toy dataset for example
# dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

segments, info = model.transcribe("audio/dbz.mp3", beam_size=1)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
