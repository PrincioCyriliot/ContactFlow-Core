# ContactFlow Core 📇

> **Un gestionnaire de contacts élégant, modulaire et persistant en Python avec stockage JSON.**

---

## 🌟 À propos de ContactFlow

**ContactFlow Core** est une application console moderne conçue pour simplifier et optimiser la gestion de votre carnet d'adresses au quotidien. Développée selon les principes de l'architecture modulaire Python, elle garantit une séparation claire entre la logique métier, l'interface utilisateur et la persistance des données.

---

## ✨ Fonctionnalités Principales

* 📋 **Listing interactif** : Visualisation claire et numérotée de l'ensemble de vos contacts
* ➕ **Ajout instantané** : Enregistrement de nouveaux contacts avec validation des saisies.
* ✏️ **Édition flexible** : Modification partielle ou totale des informations (nom, téléphone) en conservant les valeurs actuelles par défaut.
* 🗑️ **Suppression sécurisée** : Retrait ciblé d'un contact via son index.
* 🔍 **Recherche dynamique** : Recherche rapide par correspondance partielle (insensible à la casse).
* 💾 **Persistance JSON automatique** : Chargement et sauvegarde fiables dans le fichier `contacts.json`.

---

## 🏗️ Architecture du Projet

Le projet est structuré en plusieurs modules indépendants :

```text
Gestion-de-contact/
├── main.py           # Point d'entrée principal de l'application
├── menu.py           # Interface du menu et boucle d'interaction
├── contacts.py       # Logique métier (CRUD & recherche)
├── storage.py        # Gestion de la persistance (lecture/écriture JSON)
└── contacts.json     # Base de données locale au format JSON
