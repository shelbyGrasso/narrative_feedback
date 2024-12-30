import pandas as pd
import torch
from transformers import DistilBertTokenizer
from tqdm import tqdm

# Step 1: Load the TSV file
file_path = '../../data/raw_data/emolit/trn.tsv'
data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip')  # Adjust options if needed

# Inspect the data
print(data.head())

# Step 2: Select and clean the text column
# Assume the column with text is named 'text'
data['text'] = data['text'].fillna('')  # Fill missing text with empty string
data['text'] = data['text'].str.strip()  # Remove leading/trailing whitespaces

# Step 3: Initialize the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Function to tokenize a batch
def tokenize_batch(batch):
    return tokenizer(batch, padding=True, truncation=True, return_tensors="pt")


# Step 4: Process in batches
batch_size = 1000  # Adjust based on memory
output_file = '../data/processed_data/tokenized_data/processed_data.csv'

# Create a list to store processed data
processed_data = []

for i in tqdm(range(0, len(data), batch_size)):
    batch = data['text'][i:i + batch_size].tolist()
    tokenized = tokenizer(batch, padding=True, truncation=True, return_tensors="np")

    # Collect the tokenized data in the processed_data list
    for j, text in enumerate(batch):
        processed_data.append({
            'original_text': text,
            'input_ids': tokenized['input_ids'][j].tolist(),
            'attention_mask': tokenized['attention_mask'][j].tolist()
        })

# Step 5: Save to CSV
df_processed = pd.DataFrame(processed_data)
df_processed.to_csv(output_file, index=False)

print(f"Processed and tokenized data saved to {output_file}")