from flask import Flask, jsonify, request
from transformers import pipeline, BartForConditionalGeneration, BartTokenizer

summarizer = pipeline("summarization")
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)
app = Flask(__name__)

ARTICLE = """
# ... (your article text)
"""

@app.route('/summarise', methods=["POST"])
def summarise():
    input_text = request.json.get('text')
    summary = summarizer(input_text, max_length=100, min_length=60, do_sample=False)
    return jsonify({'summary': summary[0]['summary_text']})

@app.route('/api/hello', methods=['POST'])
def api_hello():
    input_text = request.json.get('text')
    print(data, input_text)
    return jsonify(data)

@app.route('/')
def get_hello():
    input_text = request.json.get('text')
    print(data, input_text)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
