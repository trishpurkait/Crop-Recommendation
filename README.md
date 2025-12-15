# 🌾 Krishi - সহায়ক: Smart Crop Recommendation System

An intelligent ML-powered web application that recommends the top 5 most suitable crops based on soil and climate parameters. This is a core module of the **Krishi Sohayak** agricultural platform aimed at helping farmers make data-driven cultivation decisions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-99.5%25-brightgreen.svg)

## 🎯 Features

- 🤖 **Machine Learning Predictions** - Random Forest Classifier with **99.5% accuracy**
- 🌾 **22 Crop Types** - Recommends from a diverse set of crops suited for various conditions
- 📊 **Top 5 Recommendations** - Shows confidence scores with visual chart representation
- 🧪 **7 Input Parameters** - Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall
- 📱 **Responsive Design** - Works seamlessly on all devices
- 🎨 **Modern UI** - Clean, agricultural-themed interface with Bootstrap 5

## 🌱 Supported Crops (22 Types)

The system can recommend from the following crops:

**Cereals & Grains:**
- Rice, Maize

**Pulses & Legumes:**
- Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil

**Fruits:**
- Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut

**Cash Crops:**
- Cotton, Jute, Coffee

## 📊 Model Performance

- **Algorithm**: Random Forest Classifier
- **Accuracy**: 99.54%
- **Cross-validation Score**: 99.49%
- **Training Dataset**: 2,200 samples
- **Test Set Performance**: Consistent high accuracy
- **Features**: 7 soil and climate parameters

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn (RandomForestClassifier)
- **Data Processing**: pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Visualization**: Chart.js
- **Deployment**: Render.com

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/trishpurkait/Crop-Recommendation.git
cd Crop-Recommendation
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

1. **Start the Flask server**
```bash
python app.py
```

2. **Open your browser**

Navigate to: `http://127.0.0.1:5000`

3. **Enter soil & climate parameters**
   - Nitrogen (N): 0 - 140
   - Phosphorus (P): 5 - 145
   - Potassium (K): 5 - 205
   - Temperature: 8°C - 44°C
   - Humidity: 15% - 100%
   - pH: 3.5 - 10
   - Rainfall: 20mm - 300mm

4. **View Results** 🎉
   - Top recommended crop
   - Top 5 crops with confidence scores
   - Interactive confidence chart

## 📁 Project Structure

```
Crop-Recommendation/
│
├── app.py                      # Main Flask application
├── model.pkl                   # Trained Random Forest model
├── le.pkl                      # Label Encoder for crop names
├── index.html                  # Web interface
├── requirements.txt            # Python dependencies
├── crop.csv                    # Training dataset (2,200 samples)
└── README.md                   # Project documentation
```

## 📦 Dependencies

```txt
Flask==3.0.0
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.24.3
```

## 🎓 How It Works

1. **Input Collection**: User enters 7 soil and climate parameters
2. **Preprocessing**: StandardScaler normalizes the input features
3. **Prediction**: Random Forest model predicts probabilities for all 22 crops
4. **Ranking**: Crops are ranked by confidence scores
5. **Display**: Top 5 recommendations shown with visual confidence chart

## 🧪 Model Training Details

The Random Forest model was trained with:
- **2,200 samples** from agricultural dataset
- **80-20 train-test split**
- **StandardScaler** for feature normalization
- **GridSearchCV** for hyperparameter tuning
- **5-fold cross-validation**
- **Random state: 42** for reproducibility

### Model Comparison Results:
- Random Forest: **99.49%** ✅ (Selected)
- SVM: 98.18%
- KNN: 97.78%

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues & Limitations

- Model trained on specific regional data (may need retraining for different regions)
- Requires all 7 parameters (no partial input support)
- Dataset limited to 22 crop types
- Does not account for market prices or economic factors

## 🔮 Future Enhancements

- [ ] Add more crop varieties (50+ crops)
- [ ] Include soil quality indicators
- [ ] Market price predictions
- [ ] Regional customization
- [ ] Multi-language support (Hindi, Bengali, regional languages)
- [ ] Historical data tracking
- [ ] Weather API integration for real-time data
- [ ] Mobile app version
- [ ] Integration with other Krishi Sohayak modules
- [ ] Expert consultation feature

## 🌾 About Krishi Sohayak

This Crop Recommendation System is part of **Krishi Sohayak** (Agricultural Assistant), a comprehensive platform designed to help farmers with:
- Intelligent crop recommendations
- Plant disease detection and treatment
- Soil health analysis
- Weather-based farming advice
- Market insights
- Expert consultation services

## 📊 Dataset Information

**Source**: Agricultural research data
- **Total Samples**: 2,200
- **Features**: 7 (N, P, K, Temperature, Humidity, pH, Rainfall)
- **Target Classes**: 22 crops
- **No Missing Values**: Complete dataset
- **No Duplicates**: Clean data

## 👥 Author

**Trish Purkait**
- GitHub: [@trishpurkait](https://github.com/trishpurkait)
- Email: trishpurkait@gmail.com

## 🙏 Acknowledgments

- Agricultural dataset contributors
- scikit-learn team for ML framework
- Bootstrap team for UI framework
- All farmers who inspire this work

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Email: trishpurkait@gmail.com
- Contributions and feedback are always welcome!

## 📈 Statistics

- ⭐ **Accuracy**: 99.54%
- 🌾 **Crops Supported**: 22
- 📊 **Dataset Size**: 2,200 samples
- 🎯 **Parameters**: 7 features
- 🚀 **Deployment**: Live on Render.com

## ⭐ Show Your Support

If you find this project useful, please consider:
- Giving it a ⭐ star on GitHub
- Sharing it with others who might benefit
- Contributing to its development
- Providing feedback for improvements

---

<p align="center">Made with ❤️ for farmers and sustainable agriculture</p>
<p align="center">© 2025 Krishi - সহায়ক | Smart Crop Recommendation System</p>
<p align="center">Part of the Krishi Sohayak Project</p>
