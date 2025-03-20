import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app  # Assure-toi d'importer correctement l'application Flask
from unittest.mock import patch
import json

@pytest.fixture
def client():
    """Fixture pour le client de test Flask."""
    app.testing = True
    with app.test_client() as client:
        yield client

# Test 1: Test de la route "/predict" avec des données valides
def test_predict_valid_data(client):
    # Données de test valides
    test_data = {
        'Age': 35,
        'Account_Manager': 1,
        'Years': 10,
        'Num_Sites': 5
    }

    # Simuler la requête POST
    response = client.post('/predict', data=test_data)

    # Vérifier que le code de statut est 200
    assert response.status_code == 200

    # Vérifier que la réponse est un JSON et contient la prédiction
    response_json = json.loads(response.data)
    assert 'churn_prediction' in response_json

# Test 2: Test de la route "/predict" avec des données manquantes
def test_predict_missing_data(client):
    # Données incomplètes (par exemple, manque 'Age')
    test_data = {
        'Account_Manager': 1,
        'Years': 10,
        'Num_Sites': 5
    }

    # Simuler la requête POST
    response = client.post('/predict', data=test_data)

    # Vérifier que le code de statut est 400 (erreur)
    assert response.status_code == 400

    # Vérifier que la réponse contient un message d'erreur
    response_json = json.loads(response.data)
    assert 'error' in response_json

# Test 3: Test de la route "/predict" avec des valeurs invalides
def test_predict_invalid_data(client):
    # Données invalides (par exemple, un âge négatif)
    test_data = {
        'Age': 15,
        'Account_Manager': 1,
        'Years': 10,
        'Num_Sites': 5
    }

    # Simuler la requête POST
    response = client.post('/predict', data=test_data)

    # Vérifier que le code de statut est 400 pour une mauvaise requête
    assert response.status_code == 400

    # Vérifier que la réponse contient un message d'erreur
    response_json = json.loads(response.data)
    assert 'error' in response_json

# Test 4: Vérification de la route d'accueil "/"
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  # Vérifie si le contenu HTML est bien rendu

# Test 5: Mocking de la prédiction du modèle
@patch('app.model.predict')  # On simule le modèle pour ne pas dépendre du vrai modèle
def test_predict_mocked(model_predict_mock, client):
    # On simule la prédiction pour qu'elle retourne une valeur prédéfinie
    model_predict_mock.return_value = [1]

    test_data = {
        'Age': 30,
        'Account_Manager': 1,
        'Years': 5,
        'Num_Sites': 3
    }

    response = client.post('/predict', data=test_data)

    # Vérifier que la réponse est correcte
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['churn_prediction'] == 1  # La valeur simulée par le mock
