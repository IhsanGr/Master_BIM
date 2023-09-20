#TP 2 : Bases de données

#Exercices

#1/ Liste des tables de la base de données

''' \d : donne liste des tables'''

#2/ Liste de la description pour chaque table

''' \d table : donne la description de la table'''

#3/ Schéma Entité/ Association de la base

'''Il est dans le dossier'''

#4/ Liste des populations dans la base

''' SELECT nom_population FROM populations ;'''

#5/ Nombre de régions différentes

''' SELECT count(regions.nom_region) FROM regions ; '''

#6/ Liste des populations européennes dans la base

''' SELECT nom_population FROM populations WHERE populations.nom_region = 'europe' ; '''

#7/ Nb de populations d'Europe

''' SELECT count(nom_population) FROM populations WHERE populations.nom_region = 'europe' '''

#8/ Liste des échantillons de taille supérieure à 300

''' SELECT nom_echantillon FROM echantillons WHERE taille_echantillon > 300 ; '''

#9/ Nb d'échantillons dont la taille est comprise entre 100 et 200 (exclus)

''' SELECT count(taille_echantillon) FROM echantillons WHERE taille_echantillon > 100 AND taille_echantillon < 200 ; '''

#10/ Liste des populations par région

''' SELECT regions, nom_population FROM regions NATURAL JOIN populations ; '''

#11/ Liste des chr à partir de la table bandes

''' SELECT chromosomes FROM bandes NATURAL JOIN chromosomes ; '''

#12/ Liste des chromosomes uniques à partir de la table bandes

''' SELECT DISTINCT chromosomes FROM bandes NATURAL JOIN chromosomes ; '''

#13/ échantillons nommés Zoro

''' SELECT nom_echantillon, echantillon_uid, taille_echantillon, pop_uid FROM echantillons NATURAL JOIN populations WHERE nom_echantillon = 'Zoro' ; '''

#14/ échantillons commençant par Druze

''' SELECT nom_echantillon, echantillon_uid FROM echantillons WHERE nom_echantillon ~ '^Druze' ; '''

#15/ échantillons contenant Afric

''' SELECT nom_echantillon, echantillons_uid FROM echantillons WHERE nom_echantillon ~ '%Afric%' ; '''