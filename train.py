# Sixth test
import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump

# Charger les données
data = pd.read_csv("data/customer_churn.csv")

X = data[['Age', 'Account_Manager', 'Years', 'Num_Sites']]

# Sélectionner la colonne cible
y = data['Churn']

# Créer et entraîner le modèle de régression logistique
model = LogisticRegression()

# Entraîner le modèle sur les données
model.fit(X, y)

# Sauvegarder le modèle entraîné avec joblib (sans dépendances pandas)
#dump(model, 'data/trained_model.pkl') 
dump(model, 'data/trained_model.pkl')
