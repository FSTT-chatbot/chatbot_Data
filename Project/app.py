from flask import Flask, request, jsonify, render_template
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

# Load model and tokenizer
model_dir = './model'
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = tokenizer(data['text'], return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    # Assuming the model returns logits, convert them to probabilities
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return jsonify(probabilities.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
