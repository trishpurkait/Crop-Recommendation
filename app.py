# app.py

from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)
enc='le.pkl'
with open(enc, 'rb') as file:
    le = pickle.load(file)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    probs = model.predict_proba(final_features)[0]
    classes = le.inverse_transform(model.classes_)
    predictions = list(zip(classes, probs))
    filtered = [(cls, p) for cls, p in predictions if p > 0.25]
    filtered_sorted = sorted(filtered, key=lambda x: x[1], reverse=True)
    top5 = filtered_sorted[:5]
    output_text = "Prediction:\n"
    for cls, p in top5:
        output_text += f"{cls} with confidence: {p*100:.2f}%\n"
    return render_template('index.html', prediction_text=output_text)

if __name__ == "__main__":
    app.run(debug=True)