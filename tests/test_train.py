import os
from joblib import load
from sklearn.linear_model import LogisticRegression

def check_pickle_file_exists(picklefile):
  assert os.path.exists(picklefile), (
    "Le fichier trained_model.pkl est introuvable"
  )

def check_input_file_exists(csvfile):
  assert os.path.exists(csvfile), (
    "Le fichier csv d'entrée est introuvable"
  )

def test_train_model_loading(model):
  assert isinstance(model, LogisticRegression), (
    "Le modèle n'est pas une régression logistique" 
  )

picklefile = "data/trained_model.pkl"
csvfile = "data/customer_churn.csv"
model = load('data/trained_model.pkl')

check_pickle_file_exists(picklefile)
check_input_file_exists(csvfile)
test_train_model_loading(model)
