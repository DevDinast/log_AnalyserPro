#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module 1 – Ingestion et Analyse des logs
Ce module :
- Scanne un dossier de fichiers .log
- Filtre les lignes selon le niveau demandé (ERROR, WARN, INFO, ALL)
- Calcule les statistiques :
    - Total de lignes analysées
    - Comptage par niveau
    - Top 5 des messages ERROR les plus fréquents
- Prépare les métadonnées (OS et utilisateur)
"""

import os
import glob
import platform
import argparse
import collections

def parser_arguments():
    """
    Parse les arguments CLI :
    --source : chemin vers le dossier contenant les logs (obligatoire)
    --niveau : niveau de filtrage parmi ERROR, WARN, INFO, ALL (défaut ALL)
    """
    parser = argparse.ArgumentParser(description="LogAnalyzer Pro - Module 1 : Analyse des logs")
    parser.add_argument("--source", required=True, help="Chemin du dossier contenant les fichiers logs")
    parser.add_argument("--niveau", choices=["ERROR","WARN","INFO","ALL"], default="ALL",
                        help="Niveau de filtrage (ERROR, WARN, INFO, ALL)")
    return parser.parse_args()


def valider_dossier(dossier):
    """
    Vérifie que le dossier existe et est bien un répertoire.
    Retourne le chemin absolu du dossier.
    """
    if os.path.exists(dossier) and os.path.isdir(dossier):
        return os.path.abspath(dossier)
    else:
        raise FileNotFoundError(f"Erreur : le dossier '{dossier}' n'existe pas ou n'est pas un dossier.")


def analyser_logs(dossier, niveau="ALL"):
    """
    Scanne tous les fichiers .log dans le dossier, filtre selon le niveau demandé,
    et retourne :
    - stats : dict(total_lignes, par_niveau, top5_erreurs)
    - fichiers_traites : liste des fichiers analysés
    - metadata : dict(os, utilisateur, source)
    """
    fichiers_traites = glob.glob(os.path.join(dossier, "*.log"))
    total_lignes = 0
    compteur_niveaux = {"ERROR": 0, "WARN": 0, "INFO": 0}
    erreurs_counter = collections.Counter()

    for fichier in fichiers_traites:
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                for ligne in f:
                    ligne = ligne.strip()
                    if not ligne:
                        continue
                    # Extraction du niveau : 3ème mot (après date et heure)
                    try:
                        parties = ligne.split(" ", 3)
                        niveau_ligne = parties[2]
                        message = parties[3] if len(parties) > 3 else ""
                    except IndexError:
                        continue  # ignorer lignes mal formées

                    # Filtrage selon le niveau demandé
                    if niveau == "ALL" or niveau_ligne == niveau:
                        total_lignes += 1
                        if niveau_ligne in compteur_niveaux:
                            compteur_niveaux[niveau_ligne] += 1
                        if niveau_ligne == "ERROR":
                            erreurs_counter[message] += 1
        except Exception as e:
            print(f"Erreur lecture fichier {fichier}: {e}")

    # Top 5 erreurs les plus fréquentes
    top5_erreurs = [msg for msg, _ in erreurs_counter.most_common(5)]

    # Métadonnées
    metadata = {
        "os": platform.system(),
        "utilisateur": os.environ.get("USER") or os.environ.get("USERNAME") or "inconnu",
        "source": os.path.abspath(dossier)
    }

    stats = {
        "total_lignes": total_lignes,
        "par_niveau": compteur_niveaux,
        "top5_erreurs": top5_erreurs
    }

    return stats, fichiers_traites, metadata


# Point d'entrée
if __name__ == "__main__":
    args = parser_arguments()
    dossier_valide = valider_dossier(args.source)
    stats, fichiers, metadata = analyser_logs(dossier_valide, args.niveau)

    # Affichage résumé
    print("=== Statistiques ===")
    print(f"Total de lignes : {stats['total_lignes']}")
    print(f"Par niveau : {stats['par_niveau']}")
    print(f"Top 5 erreurs : {stats['top5_erreurs']}")
    print(f"Fichiers analysés : {fichiers}")
    print(f"Métadonnées : {metadata}")