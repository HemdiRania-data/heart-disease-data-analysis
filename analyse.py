import pandas as pd
 
fichier = "processed.cleveland.data"
 
data = pd.read_csv(
    fichier,
    header=None,
    na_values="?"
)
 
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
 
print("\nPremières lignes :")
print(data.head())
 
print("\nDimensions du dataset :")
print(data.shape)
 
print("\nTypes des variables :")
print(data.dtypes)
 
print("\nValeurs manquantes :")
print(data.isnull().sum())
 
print("\nStatistiques descriptives :")
print(data.describe())
 
print("\nRépartition de la maladie cardiaque :")
print(data["target"].value_counts())
 
print("\nValeurs uniques par variable :")
for colonne in data.columns:
    print(f"\n{colonne} :")
    print(data[colonne].unique())
 
print("\nType et nombre de modalités par variable :")
for colonne in data.columns:
    print(
        f"{colonne} : type={data[colonne].dtype}, "
        f"modalités={data[colonne].nunique()}"
    )
 
