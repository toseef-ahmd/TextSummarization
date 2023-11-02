import pandas as pd
from datasets import load_dataset
from apirequest import summary_api_request
import re
from graph import get_overall_graph,get_all_graphs
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

results = []


def calculate_rouge_scores(hypothesis, reference):
    # Calculate ROUGE-2 and ROUGE-3 scores
    smoothing = SmoothingFunction().method4  # Smoothing function for short sentences
    rouge2_s = corpus_bleu([[reference]], [hypothesis], weights=(0.5, 0.5), smoothing_function=smoothing)
    rouge3_s = corpus_bleu([[reference]], [hypothesis], weights=(1 / 3, 1 / 3, 1 / 3), smoothing_function=smoothing)
    return rouge2_s, rouge3_s


dataset = load_dataset("cnn_dailymail", '3.0.0')
train_data = dataset['train']
first_example = train_data[2]

for i in range(300):
    example = train_data[i]
    article = example["article"]
    highlights = example["highlights"]
    total_sentences = len(re.split(r'(?<=[.!?])\s', highlights))
    json_response = summary_api_request(article, length=total_sentences)

    rouge2_score, rouge3_score = calculate_rouge_scores(json_response["TextRank"], highlights)
    lsa_rouge2, lsa_rouge3 = calculate_rouge_scores(json_response["LSA"], highlights)
    relevance_rouge2, relevance_rouge3 = calculate_rouge_scores(json_response["Relevance"], highlights)

    results.append({
        "Index": i,
        "TextRank ROUGE-2": rouge2_score,
        "TextRank ROUGE-3": rouge3_score,
        "LSA ROUGE-2": lsa_rouge2,
        "LSA ROUGE-3": lsa_rouge3,
        "Relevance ROUGE-2": relevance_rouge2,
        "Relevance ROUGE-3": relevance_rouge3
    })

df = pd.DataFrame(results)
df.to_csv('results.csv', index=False)

get_overall_graph(df)
get_all_graphs(df)