# Script Python : Mouvement Aléatoire de la Souris & Simulation de Touches

Ce script Python simule des pressions aléatoires sur les touches `Z`, `Q`, `S`, `D` et déplace la souris de manière aléatoire toutes les 2 à 3 minutes.

## 🛠️ Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les dépendances nécessaires :

- Python 3.x
- Bibliothèques requises (installables via `pip`) :

```bash
pip install pynput
```

## 📜 Installation

1. Clonez ce dépôt :

```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

Exécutez le script avec :

```bash
python script.py
```

Une fois en cours d'exécution :

- Le script simule la pression aléatoire des touches `Z`, `Q`, `S`, `D` à un intervalle variable.
- Toutes les 2 à 3 minutes, la souris est déplacée à une position aléatoire.

### Exemple de Fonctionnement

- Une touche est pressée et relâchée pendant une durée aléatoire.
- Tous les 5 essais, un message affiche le nombre total de pressions de touches.
- La souris est déplacée à des coordonnées aléatoires en ajoutant un décalage compris entre -100 et 100 pixels sur les axes X et Y.

## 🛑 Arrêt du script

Pour arrêter le script, utilisez **CTRL + C** dans le terminal ou fermez la fenêtre d'exécution.

## 📌 Notes

- Ce script utilise `pynput` pour simuler les pressions de touches et les mouvements de souris.
- Il fonctionne uniquement sur les systèmes où `pynput` est pris en charge (Windows/Linux/Mac).
- Assurez-vous d'exécuter le script avec les permissions nécessaires si vous rencontrez des erreurs.
