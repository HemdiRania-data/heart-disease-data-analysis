import pandas as pd

fichier = "processed.cleveland.data"

data = pd.read_csv(fichier, header=None)

data.columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target"
]

print(data.head())
print(data.columns)

print("\nRépartition de la maladie cardiaque :")
print(data["target"].value_counts())