from flask import Flask, render_template, request, jsonify
from pytldr.summarize.lsa import LsaSummarizer
from pytldr.summarize.relevance import RelevanceSummarizer
from pytldr.summarize.textrank import TextRankSummarizer
import requests

app = Flask(__name__)


# TextRank Summarizer
def text_rank_summary(text_to_summarize, len):
    textrank = TextRankSummarizer()
    summary = textrank.summarize(text_to_summarize, length=len)
    summary_textrank = ' '.join(summary)
    return summary_textrank


# LSA Summarizer
def lsa_summary(text_to_summarize, len):
    relevance = RelevanceSummarizer()
    summary = relevance.summarize(text_to_summarize, length=len)
    summary_relevance = ' '.join(summary)
    return summary_relevance


# Relevance Summarizer (using LexRank)
def relevance_summary(text_to_summarize, len=3):
    lsa = LsaSummarizer()
    summary = lsa.summarize(text_to_summarize, length=len)
    summary_lsa = ' '.join(summary)
    return summary_lsa


@app.route('/summary', methods=['POST'])
def summarize():
    data = request.get_json()  # Assuming you will send a JSON object with a 'text' key
    text_to_summarize = data.get('text', '')
    len = data.get('length', 3)
    uploaded_text = None  # Define the variable here with a default value

    print("TEXT TO SUMMARIZE " + "LENGTH " + str(len) + text_to_summarize)

    summary_textrank = text_rank_summary(text_to_summarize, len)

    summary_relevance = lsa_summary(text_to_summarize, len)

    summary_lsa = relevance_summary(text_to_summarize, len)

    summary_data = {
        "TextRank": summary_textrank,
        "LSA": summary_lsa,
        "Relevance": summary_relevance
    }

    return jsonify(summary_data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def get_summary():
    document_link = request.form.get('link')
    uploaded_file = request.files.get('file')
    if uploaded_file:
        # Read the content of the uploaded text file
        text = uploaded_file.read()
        uploaded_text = text.decode('utf-8', errors='ignore')
    elif document_link:
        # Fetch content from the provided link
        document_link = document_link.replace('https://', 'http://')
        response = requests.get(document_link)
        if response.status_code == 200:
            uploaded_text = response.text  # Get the text content from the link
        else:
            # Handle the case where the link is not valid
            error_message = "Invalid link. Please check the URL."
            return render_template('index.html', error_message=error_message)
    text_to_summarize = uploaded_text if uploaded_file else document_link

    data = {"text": text_to_summarize, "length": 3}
    summary_response = requests.post('http://localhost:5000/summary', json=data)

    # summary_response = summarize(text_to_summarize)  # Store the JSON response
    summary_data = summary_response.json()  # Get the JSON data

    return render_template('index.html', summary_textrank=summary_data['TextRank'],
                           summary_relevance=summary_data['Relevance'],  # Fix this line
                           summary_lsa=summary_data['LSA'])  # Fix this line


if __name__ == '__main__':
    app.run(debug=True)
