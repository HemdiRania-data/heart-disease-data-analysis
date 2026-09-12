# Heart Disease Data Analysis

Analyse clinique et exploration du dataset **UCI Heart Disease** (base Cleveland) : nettoyage, exploration statistique et visualisation en vue d'une future modélisation prédictive de la maladie cardiaque.

## Objectif du projet

Explorer les facteurs cliniques associés à la présence d'une maladie cardiaque à partir de 303 patients, et préparer les données pour une classification (malade / non malade).

## Données utilisées

- **Source** : [UCI Machine Learning Repository – Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
- **Fichier utilisé** : `processed.cleveland.data`
- 303 observations, 13 variables cliniques + 1 variable cible (`target`)

| Variable | Description |
|---|---|
| age | Âge du patient |
| sex | Sexe (1 = homme, 0 = femme) |
| cp | Type de douleur thoracique (1 à 4) |
| trestbps | Tension artérielle au repos (mm Hg) |
| chol | Cholestérol sérique (mg/dl) |
| fbs | Glycémie à jeun > 120 mg/dl (1 = vrai) |
| restecg | Résultat ECG au repos |
| thalach | Fréquence cardiaque maximale atteinte |
| exang | Angine induite par l'effort (1 = oui) |
| oldpeak | Dépression du segment ST induite par l'effort |
| slope | Pente du segment ST à l'effort |
| ca | Nombre de vaisseaux principaux colorés (0-3) |
| thal | Thalassémie (3 = normal, 6 = défaut fixe, 7 = défaut réversible) |
| target | 0 = absence de maladie, 1-4 = présence (degré de sévérité) |

## Méthodologie

### 1. Exploration initiale (`analyse.py`)
Chargement des données, vérification des types, détection des valeurs manquantes, statistiques descriptives et inventaire des modalités par variable.

### 2. Nettoyage (`nettoyage_visualisation.py`)
- Suppression des 6 lignes contenant des valeurs manquantes (`ca`, `thal`) — soit 2 % du jeu de données
- Conversion des variables catégorielles (`sex`, `cp`, `fbs`, `restecg`, `exang`, `slope`, `ca`, `thal`) au bon type
- Création d'une cible binaire `target_bin` (0 = pas de maladie, 1 = maladie, tous degrés confondus)
- Export du jeu de données nettoyé : `cleveland_clean.csv`

### 3. Visualisation
Histogrammes, matrice de corrélation, boxplots et répartitions catégorielles pour identifier les variables les plus discriminantes.

## Résultats clés

### Distributions par classe cible

![Histogrammes des variables continues](images/histogrammes.png)

`thalach` (fréquence cardiaque max) et `oldpeak` (dépression ST) montrent une séparation visible entre patients malades et non malades — ce sont les deux variables continues les plus prometteuses pour la suite.

### Corrélations

![Matrice de corrélation](images/correlation.png)

`oldpeak` (+0.50) et `thalach` (-0.42) sont les variables les plus corrélées à la cible. À l'inverse, `chol` (0.07) et `trestbps` (0.16) le sont étonnamment peu, malgré leur réputation de facteurs de risque cardiovasculaire classiques.

### Valeurs extrêmes

![Boxplots](images/boxplots.png)

Quelques outliers à surveiller pour la modélisation : un cholestérol proche de 560 mg/dl, un `oldpeak` à 6.2, et une fréquence cardiaque max anormalement basse (~71).

### Répartition selon le sexe et le type de douleur thoracique

![Répartition catégorielle](images/repartition_categorielle.png)

Les hommes sont proportionnellement plus touchés dans cet échantillon (mais aussi surreprésentés dans les données globales). Le type de douleur thoracique `cp=4` (asymptomatique) est fortement associé à la présence de maladie — une catégorie clinique contre-intuitive à ce nom.

## Prochaines étapes

- [ ] Standardisation des variables continues
- [ ] Séparation train / test stratifiée
- [ ] Modèles de classification : régression logistique (baseline), arbre de décision, random forest
- [ ] Évaluation via accuracy, matrice de confusion et recall (priorité à la détection des vrais malades)

## Installation et exécution

```bash
git clone https://github.com/HemdiRania-data/heart-disease-data-analysis.git
cd heart-disease-data-analysis
pip install -r requirements.txt
python analyse.py
python nettoyage_visualisation.py
```

## Structure du projet

```
heart-disease-data-analysis/
├── data/
│   └── processed.cleveland.data
├── images/
│   ├── histogrammes.png
│   ├── correlation.png
│   ├── boxplots.png
│   └── repartition_categorielle.png
├── analyse.py
├── nettoyage_visualisation.py
├── cleveland_clean.csv
├── requirements.txt
└── README.md
```
