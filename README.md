# 📊 LogAnalyzer Pro — Pipeline d’Analyse et d’Archivage de Logs

## 1. Description du projet

**LogAnalyzer Pro** est un outil en ligne de commande (CLI) développé en Python permettant d’analyser des fichiers de logs applicatifs, de générer des rapports structurés au format JSON, d’archiver les logs traités et de nettoyer automatiquement les anciens rapports.

Ce projet s’inscrit dans un contexte **DevOps / administration système**, où l’automatisation du traitement des logs est essentielle pour la supervision et la maintenance des systèmes.

---

## 2. Objectifs

* Analyser des fichiers de logs contenant différents niveaux de criticité (INFO, WARN, ERROR)
* Générer des statistiques exploitables
* Produire un rapport JSON structuré
* Archiver les fichiers traités
* Nettoyer les anciens rapports
* Automatiser l’exécution via Cron

---

## 3. Prérequis

* Python 3.x installé
* Aucune dépendance externe (utilisation exclusive de la bibliothèque standard)

---

## 4. Structure du projet

```
LogAnalyzerPro/
├── main.py
├── analyser.py
├── rapport.py
├── archiver.py
├── logs_test/
│   ├── app1.log
│   ├── app2.log
│   └── app3.log
├── rapports/
├── backups/
└── README.md
```

---

## 5. Format des logs

Chaque ligne de log doit respecter le format suivant :

```
YYYY-MM-DD HH:MM:SS NIVEAU Message
```

### Exemple :

```
2024-04-01 08:22:30 ERROR Échec de la connexion au serveur LDAP
2024-04-01 08:30:00 INFO Tâche planifiée démarrée
2024-04-01 09:00:01 WARN Utilisation CPU élevée
```

---

## 6. Utilisation

### ▶️ Commande de base

```
python3 main.py --source logs_test
```

### ▶️ Avec filtrage par niveau

```
python3 main.py --source logs_test --niveau ERROR
```

### Paramètres disponibles :

| Argument | Description                                        |
| -------- | -------------------------------------------------- |
| --source | Chemin du dossier contenant les logs (obligatoire) |
| --niveau | Niveau de filtrage : ERROR, WARN, INFO, ALL        |

---

## 7. Fonctionnement du pipeline

```
Logs → Analyse → Statistiques → JSON → Archivage → Nettoyage
```

### Étapes détaillées :

1. Scan des fichiers `.log`
2. Lecture ligne par ligne
3. Filtrage par niveau
4. Calcul des statistiques :

   * Nombre total de lignes
   * Comptage par niveau
   * Top 5 erreurs
5. Génération d’un rapport JSON
6. Archivage des logs en `.tar.gz`
7. Suppression des anciens rapports

---

## 8. Structure du rapport JSON

Exemple de sortie :

```json
{
  "metadata": {
    "date": "2026-03-25 10:30:00",
    "utilisateur": "user",
    "os": "Linux",
    "source": "/chemin/logs_test"
  },
  "statistiques": {
    "total_lignes": 120,
    "par_niveau": {
      "ERROR": 30,
      "WARN": 40,
      "INFO": 50
    },
    "top5_erreurs": [
      "Erreur DB",
      "Connexion refusée"
    ]
  },
  "fichiers_traites": [
    "app1.log",
    "app2.log"
  ]
}
```

---

## 9. Automatisation avec Cron

### Exécution chaque dimanche à 03h00 :

```
0 3 * * 0 /usr/bin/python3 /chemin/absolu/main.py --source /chemin/logs
```

### Explication :

| Champ | Valeur       | Signification  |
| ----- | ------------ | -------------- |
| 0     | minute       | à la minute 0  |
| 3     | heure        | à 03h du matin |
| *     | jour         | tous les jours |
| *     | mois         | tous les mois  |
| 0     | jour semaine | dimanche       |

---

## 10. Gestion des erreurs

Le système gère plusieurs cas :

* Dossier source inexistant
* Fichiers logs mal formatés
* Problèmes de lecture de fichiers
* Espace disque insuffisant

---

## 11. Modules du projet

### analyser.py

* Analyse des logs
* Calcul des statistiques

### rapport.py

* Génération du rapport JSON

### archiver.py

* Archivage des logs
* Nettoyage automatique

### main.py

* Orchestration complète
* Gestion des erreurs

---

## 12. Points forts du projet

* Architecture modulaire claire
* Utilisation exclusive de la bibliothèque standard
* Pipeline automatisé complet
* Compatible environnement réel (Cron)
* Gestion robuste des erreurs

---

## 13. Répartition des tâches

Ce projet a été fait dans son entierete par HOUNDJI ENABOUA JOHN ROSS

---

## 14. Conclusion

LogAnalyzer Pro simule un outil réel utilisé en environnement DevOps pour la supervision des logs.
Le projet met en œuvre des concepts clés : automatisation, traitement de fichiers, structuration des données et robustesse système.

---
