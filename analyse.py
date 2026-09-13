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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# ============================================================
# 1. CHARGEMENT
# ============================================================
fichier = "processed.cleveland.data"
 
data = pd.read_csv(
    fichier,
    header=None,
    na_values="?"
)
 
data.columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
]
 
print(f"Dimensions avant nettoyage : {data.shape}")
 
# ============================================================
# 2. NETTOYAGE
# ============================================================
 
# --- 2.1 Valeurs manquantes (ca: 4, thal: 2) ---
# Choix : suppression des lignes concernées (perte minime : 6/303 = ~2%)
data = data.dropna(subset=["ca", "thal"]).reset_index(drop=True)
print(f"Dimensions après suppression des NaN : {data.shape}")
 
# --- 2.2 Typage des variables catégorielles ---
categorielles = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]
for col in categorielles:
    data[col] = data[col].astype(int).astype("category")
 
# --- 2.3 Cible binaire pour la classification simple ---
# target original : 0 = pas de maladie, 1-4 = degrés de sévérité
data["target_bin"] = (data["target"] > 0).astype(int)
 
print("\nRépartition cible binaire :")
print(data["target_bin"].value_counts())
 
print("\nTypes après nettoyage :")
print(data.dtypes)
 
# Sauvegarde du jeu de données nettoyé pour la suite du projet
data.to_csv("cleveland_clean.csv", index=False)
print("\nFichier nettoyé sauvegardé : cleveland_clean.csv")
sns.set_style("whitegrid")
 
# --- 3.1 Histogrammes des variables continues par classe cible ---
continues = ["age", "trestbps", "chol", "thalach", "oldpeak"]
 
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
axes = axes.flatten()
for i, col in enumerate(continues):
    sns.histplot(
        data=data, x=col, hue="target_bin",
        kde=True, ax=axes[i], palette=["#4C72B0", "#C44E52"],
        element="step", common_norm=False
    )
    axes[i].set_title(f"Distribution de {col}")
axes[-1].axis("off")
plt.tight_layout()
plt.savefig("histogrammes.png", dpi=120)
plt.close()
print("Sauvegardé : histogrammes.png")
 
# --- 3.2 Matrice de corrélation (variables numériques) ---
plt.figure(figsize=(10, 8))
corr = data[continues + ["target"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, square=True)
plt.title("Matrice de corrélation (variables continues)")
plt.tight_layout()
plt.savefig("correlation.png", dpi=120)
plt.close()
print("Sauvegardé : correlation.png")
 
# --- 3.3 Boxplots pour repérer les outliers ---
fig, axes = plt.subplots(1, len(continues), figsize=(18, 5))
for i, col in enumerate(continues):
    sns.boxplot(data=data, y=col, ax=axes[i], color="#4C72B0")
    axes[i].set_title(col)
plt.tight_layout()
plt.savefig("boxplots.png", dpi=120)
plt.close()
print("Sauvegardé : boxplots.png")
 
# --- 3.4 Répartition de la cible selon sex et cp ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(data=data, x="sex", hue="target_bin", ax=axes[0], palette=["#4C72B0", "#C44E52"])
axes[0].set_title("Maladie cardiaque selon le sexe (0=F, 1=H)")
sns.countplot(data=data, x="cp", hue="target_bin", ax=axes[1], palette=["#4C72B0", "#C44E52"])
axes[1].set_title("Maladie cardiaque selon le type de douleur thoracique (cp)")
plt.tight_layout()
plt.savefig("repartition_categorielle.png", dpi=120)
plt.close()
print("Sauvegardé : repartition_categorielle.png")
 
