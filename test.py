from langchain.text_splitter import CharacterTextSplitter

# Some text to split
long_text = ("a" * 200)

# 1. Initialize the splitter
text_splitter = CharacterTextSplitter(
    separator="\n",  # We'll keep this simple for now
    chunk_size = 120,  # Max characters per chunk
    chunk_overlap  = 20,  # Overlap between chunks
    length_function=len,
)

# 2. Split the text
chunks = text_splitter.split_text(long_text)

# 3. Inspect the chunks
print(f"Original text length: {len(long_text)}")
print(f"Split into {len(chunks)} chunks.")
print("-" * 20)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} (length: {len(chunk)}):\n\"{chunk}\"")
    print("-" * 20)