from transformers import DistilBertForSequenceClassification, DistilBertTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load the preprocessed dataset (replace with your actual file path)
dataset = load_dataset("csv", data_files="../data/processed_data/tokenized_data/processed_data.csv")

# Load pre-trained DistilBERT model for sequence classification
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=37)

# Load the DistilBERT tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",          # Directory to save the model
    evaluation_strategy="epoch",     # Evaluate after each epoch
    learning_rate=2e-5,              # Fine-tuning learning rate
    per_device_train_batch_size=16,  # Batch size for training
    per_device_eval_batch_size=64,   # Batch size for evaluation
    num_train_epochs=3,              # Number of training epochs
    weight_decay=0.01,               # Regularization term
)

# Tokenization function for training and testing data
def tokenize_function(examples):
    return tokenizer(examples["original_text"], padding="max_length", truncation=True)

# Apply tokenization to the entire dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("./models/trained_model")
tokenizer.save_pretrained("./models/trained_model")

print("Fine-tuning complete and saved.")
