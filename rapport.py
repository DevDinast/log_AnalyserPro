#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module 2 – Génération du rapport JSON
"""

import os
import json
from datetime import datetime

def generer_rapport(stats, fichiers_traites, metadata, dossier_rapports="rapports"):
    # Création dossier rapports si inexistant
    os.makedirs(dossier_rapports, exist_ok=True)
    
    # Nom du fichier horodaté
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    rapport_file = os.path.join(dossier_rapports, f"rapport_{date_str}.json")
    
    contenu = {
        "metadata": {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "utilisateur": metadata["utilisateur"],
            "os": metadata["os"],
            "source": metadata["source"]
        },
        "statistiques": {
            "total_lignes": stats["total_lignes"],
            "par_niveau": stats["par_niveau"],
            "top5_erreurs": stats["top5_erreurs"]
        },
        "fichiers_traites": fichiers_traites
    }
    
    with open(rapport_file, "w", encoding="utf-8") as f:
        json.dump(contenu, f, indent=4, ensure_ascii=False)
    
    return rapport_file