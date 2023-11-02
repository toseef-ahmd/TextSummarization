from datasets import load_dataset

dataset = load_dataset("cnn_dailymail", '3.0.0')
train_data = dataset['train']
first_example = train_data[252]

# Accessing the article and highlights (summary)
article = first_example["article"]
highlights = first_example["highlights"]

print("Article:")
print(article)
print("\nHighlights:")
print(highlights)
