# load_data.py
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader


web_loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
web_docs = web_loader.load()

print(f"\nLoaded {len(web_docs)} document(s) from the web page.")

# Let's inspect the loaded content
print("\n--- Content from the web page: ---")
print(web_docs[0].page_content[:400])
print("\n--- Metadata from the web page: ---")
print(web_docs[0].metadata)



# Initialize the loader with the path to your file
loader = TextLoader("./data/my_notes.txt")

# Call the load method to get the documents
docs = loader.load()

print(f"Loaded {len(docs)} document(s).")
print("\n--- Here's the content: ---")
print(docs[0].page_content)
print("\n--- And here's the metadata: ---")
print(docs[0].metadata)


# Initialize the loader for your PDF
pdf_loader = PyPDFLoader("./data/research_paper.pdf")
pages = pdf_loader.load_and_split() # This splits the PDF into pages

print(f"\nLoaded {len(pages)} pages from the PDF.")

# Let's inspect page 5 (index 4)
print("\n--- Content from page 5: ---")
print(pages[4].page_content[:400]) # Print first 400 characters
print("\n--- Metadata for page 5: ---")
print(pages[4].metadata)