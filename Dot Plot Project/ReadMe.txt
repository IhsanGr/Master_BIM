QUE FAIRE AVEC LES FICHIERS ?

Pour exécuter proprement les fichiers afin de parvenir à l'étape finale du projet il faut :

-Importer les fichiers dans un serveur psql
-Se connecter au serveur psql
-Suivre les instructions dans create_base.txt
-Exécuter le fichier DataBase.py
-Exécuter le fichier GUI.py
-Cela affichera l'interface graphique


COMMENT FONCTIONNE L'INTERFACE GRAPHIQUE ?

-Couple query-subject : menu déroulant permettant de sélectionner le couple d'espèces à comparer
			=>les espèces sélectionnables correspondent à celles présentent dans la base de données psql "projetIG"

-Ajout query-subject : deux menus déroulants permettant de sélectionner un couple d'espèces à ajouter dans la base de données psql
		       =>les espèces sélectionnables correspondent à celles présentent dans le fichier prokaryotes_complete-genomes

-ADD COUPLE : permet d'ajouter le couple d'espèces sélectionné avec l'option "Ajout query-subject"

-Pourcentage d'identité : case qui une fois cochée sélectionne les blastp selon un seuil de pourcentage d'identité défini par l'utilisateur

-Seuil identité : barre d'entrée qui permet de fixer le seuil choisi pour le critère "pourcentage d'identité"
		 =>fonctionnement similaire pour tous les autres seuils (mais le critère diffère)
/!\ Les barres d'entrée ne peuvent être remplies qu'avec des chiffres

-Taille de la fenêtre : barre d'entrée qui permet de fixer la taille de la fenêtre pour considérer deux gènes comme homologues (voir énoncé)
/!\ Ne peut être remplie qu'avec des entiers

-Seuil de stringence : barre d'entrée qui permet de fixer le seuil de stringence
/!\ Ne peut être remplie qu'avec des chiffres

/!\ Les options "Taille de la fenêtre" et "Seuil de stringence" ne fonctionnent que si elles sont toutes les deux remplies

-DRAW : Affiche un dot plot entre le couple d'espèces sélectionné avec l'option "Couple query-subject"
	=>Ce dotplot prendra en compte toutes les options activées par l'utilisateur


QUE FONT LES FICHIERS ?

-Les fichiers .py sont des fichiers de code
-Le fichier "create_base.txt" est un fichier contenant les commandes à entrer pour créer une base de données permettant de stocker toutes les informations voulues
-Le fichier "Fiche résumé question bio.odt" est un fichier résumant les conclusions biologiques suite aux résultats obtenus en utilisant la GUI
-Le fichier 
-Tout le reste sont des fichiers de données fournis par Moodle.

DataBase.py : Ce fichier permet de pré-remplir la base de données "projetIG" à partir des fichier .csv et .out

GUI.py : Ce fichier code l'interface graphique et toutes ses fonctionnalités
=>Ces deux fichiers nécessitent la présence des bibliothèques psycopg2, re, os, gzip, subprocess, glob, tkinter, numpy, matplotlib, ftplib et  numba pour fonctionner
