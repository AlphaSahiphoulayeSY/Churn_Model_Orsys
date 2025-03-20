from flask import Flask, request, jsonify, render_template
from joblib import load
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
#model = load('data/trained_model.pkl')
model = load('data/trained_model.pkl')

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  try:
    # Récupérer les données du formulaire
    age = float(request.form['Age'])
    account_manager = int(request.form['Account_Manager'])
    years = float(request.form['Years'])
    num_sites = int(request.form['Num_Sites'])

    # Créer un tableau numpy pour les données
    features = np.array([[age, account_manager, years, num_sites]])

    # Effectuer la prédiction
    prediction = model.predict(features)
    result = int(prediction[0])

    # Retourner la réponse sous format de JSON
    return jsonify({'churn_prediction': result})
    
  except Exception as e:
    return jsonify({'error': str(e)}), 400

# Lancer l'application
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5012, debug=True)