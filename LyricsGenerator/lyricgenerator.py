from transformers import ( # type: ignore
    GPT2LMHeadModel,
    GPT2TokenizerFast,
    pipeline
)
import torch # type: ignore
import sys

checkpoint_path = "./model_checkpoint"
tokenizer = GPT2TokenizerFast.from_pretrained(checkpoint_path)
model = GPT2LMHeadModel.from_pretrained(checkpoint_path)

# find the correct device
device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
model = model.to(device)
model.eval()

swiftgpt = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

# Get starting lyrics from command line argument
if len(sys.argv) < 2:
    print("Usage: python lyricgenerator.py '<starting_lyrics>'")
    sys.exit(1)

starting_lyrics = sys.argv[1]
prompt = f"<|startofsong|> {starting_lyrics}"

outputs = swiftgpt(
    prompt,
    max_length=400,
    do_sample=True,
    top_k=50,
    top_p=0.65,
    temperature=0.9,
    num_return_sequences=1,
    repetition_penalty=1.5,
    no_repeat_ngram_size=3,
)