#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module 3 – Archivage et Nettoyage
"""

import os
import tarfile
import shutil
import time
import subprocess

def verifier_espace_disque(min_mb=100):
    try:
        statvfs = os.statvfs("/")
        espace_libre_mb = (statvfs.f_frsize * statvfs.f_bavail) / (1024 * 1024)
        if espace_libre_mb < min_mb:
            raise OSError(f"Espace disque insuffisant : {espace_libre_mb:.2f} MB")
    except Exception as e:
        print(f"Erreur vérification disque: {e}")

def archiver_logs(fichiers_traites, dossier_dest="backups"):
    os.makedirs(dossier_dest, exist_ok=True)
    date_str = time.strftime("%Y-%m-%d")
    archive_file = os.path.join(dossier_dest, f"backup_{date_str}.tar.gz")
    
    with tarfile.open(archive_file, "w:gz") as tar:
        for fichier in fichiers_traites:
            tar.add(fichier, arcname=os.path.basename(fichier))
    return archive_file

def nettoyer_anciens_rapports(dossier_rapports="rapports", retention=30):
    now = time.time()
    for nom in os.listdir(dossier_rapports):
        fichier = os.path.join(dossier_rapports, nom)
        if os.path.isfile(fichier):
            age_jours = (now - os.path.getmtime(fichier)) / (24*3600)
            if age_jours > retention:
                os.remove(fichier)