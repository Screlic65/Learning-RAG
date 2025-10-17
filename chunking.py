
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Some text to split
long_text = (
    "Retrieval-Augmented Generation (RAG) is a powerful technique for enhancing LLM performance. "
    "It combines a retriever, which pulls relevant documents, with a generator LLM. "
    "This process grounds the model in facts, reducing hallucinations. The choice of chunking "
    "strategy is critical for retrieval quality. We will explore several methods."
)

# 1. Initialize the splitter
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
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