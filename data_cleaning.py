import re

def clean_text(text: str) -> str:
    """A simple function to clean text data."""
    # 1. Convert to lowercase
    text = text.lower()
    # 2. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # 3. Remove special characters and punctuation (keeping basic structure)
    text = re.sub(r'[^a-z0-9\s.,-]', '', text) # Kept dots, commas, hyphens
    # 4. Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Let's test it on a messy string
messy_text = "  <p>Hello World! <b>Welcome</b> to the year... 2024!!\n\nCheck this out.</p> "
cleaned = clean_text(messy_text)
print(f"Original: {messy_text}")
print(f"Cleaned: {cleaned}")
# Expected Output: 'hello world welcome to the year... 2024 check this out.'

