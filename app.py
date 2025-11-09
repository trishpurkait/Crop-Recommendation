from flask import Flask, request, render_template
import numpy as np
import pickle
import json

# Load model and label encoder
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('le.pkl', 'rb') as file:
    le = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        form_values = request.form.to_dict()
        input_values = {k: float(v) for k, v in form_values.items()}
        final_features = [np.array(list(input_values.values()))]

        # Predict probabilities
        probs = model.predict_proba(final_features)[0]
        class_labels = le.inverse_transform(model.classes_)

        # Combine and get top 5
        predictions = list(zip(class_labels, probs))
        top5 = sorted(predictions, key=lambda x: x[1], reverse=True)[:5]

        labels = [cls for cls, _ in top5]
        values = [round(p * 100, 2) for _, p in top5]
        top_crop = labels[0]

        return render_template(
            'index.html',
            top_crop=top_crop,
            labels=json.dumps(labels),
            values=json.dumps(values),
            prediction_text="Here are your top 5 recommended crops based on the given parameters 🌾",
            inputs=input_values
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
