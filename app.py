from flask import Flask, render_template, request
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

app = Flask(__name__)  # Fix the bug: __name__ not **name**

# Load model and tokenizer
model_path = "./fine_tuned_model"
tokenizer = DistilBertTokenizer.from_pretrained(model_path)
model = DistilBertForSequenceClassification.from_pretrained(model_path)
model.eval()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        message = request.form['message']
        inputs = tokenizer(message, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class_id = torch.argmax(logits, dim=1).item()
        prediction = "Spam" if predicted_class_id == 1 else "Ham"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
