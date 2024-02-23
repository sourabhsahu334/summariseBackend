
from flask import Flask,jsonify,request
from transformers import pipeline, BartForConditionalGeneration, BartTokenizer

summarizer = pipeline("summarization")
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)
app = Flask(__name__)

ARTICLE = """
The Budget session of the Bihar Assembly began Monday with Chief Minister Nitish Kumar moving a motion of confidence and winning it for his coalition government with the Bhartiya Janata Party (BJP).

This motion followed Nitish Kumar’s resignation from the Chief Minister position and his departure from the Congress-led Mahagathbandhan alliance.

Amid the political upheaval, Bihar Governor Rajendra Arlekar emphasised that upholding the rule of law is the foremost priority of the Nitish Kumar-led government.

INDIA
Bihar CM Nitish Kumar wins floor test with 129 MLAs in favour of coalition with BJP
The necessity for the trust vote arose after Nitish Kumar, now serving as Chief Minister for the ninth time, formed a new government in alliance with the BJP-led NDA coalition
FP Staff February 12, 2024 15:59:20 IST
Bihar CM Nitish Kumar wins floor test with 129 MLAs in favour of coalition with BJP
Nitish Kumar with his associates in Bihar Assembly. PTI

The Budget session of the Bihar Assembly began Monday with Chief Minister Nitish Kumar moving a motion of confidence and winning it for his coalition government with the Bhartiya Janata Party (BJP).

This motion followed Nitish Kumar’s resignation from the Chief Minister position and his departure from the Congress-led Mahagathbandhan alliance.

Amid the political upheaval, Bihar Governor Rajendra Arlekar emphasised that upholding the rule of law is the foremost priority of the Nitish Kumar-led government.

RELATED ARTICLES
In
In Graphics | Nitish Kumar sails through floor test in Bihar. Here’s how it works
In
5 ways UPA ruined India's economy: This is what Centre's White Paper says
He stated, “Rule of law prevails in the state… that is the top priority of the government. To improve law and order, the strength of the police force has been increased.”

The necessity for the trust vote arose after Nitish Kumar, now serving as Chief Minister for the ninth time, formed a new government in alliance with the BJP-led NDA coalition.

Media reports suggest that Nitish Kumar was disappointed after not being appointed as the convenor of the Opposition bloc, INDIA, which emerged through his efforts.

This disappointment led to his resignation as chief minister on January 28th.
"""


@app.route('/summarise',methods=["POST"])
def hello_world():  # put application's code here
    input_text = request.json.get('text');

    summary = summarizer(input_text, max_length=100, min_length=60, do_sample=False)

    # Return the summary as JSON
    return jsonify({'summary': summary[0]['summary_text']})

data = {
    "message": "Hello, World!",
    "status": "success"
}

# Define a route for the GET API
@app.route('/api/hello', methods=['POST'])
def get_hello():
    input_text = request.json.get('text');
    print(data,input_text)
    return jsonify(data)

@app.route('/')
def get_hello():
    input_text = request.json.get('text');
    print(data,input_text)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
