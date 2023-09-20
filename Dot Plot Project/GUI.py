import psycopg2, re, os, gzip, subprocess, glob
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from ftplib import FTP
from numba import njit

def readfaa(fichier, specie):
    '''
    Lit un fichier .faa et créer un dictionnaire contenant les informations de la table Genes dans la database
    '''
    D = {}
    len_seq = 0
    rang = 0

    flux = open(fichier)
    for line in flux:
        line = line.rstrip()

        if line[0] == '>' :
            if len_seq!=0 :
                D[nom] = [specie, len_seq, rang, 'Uncharacterized protein']
                rang+=1
                nom = re.findall("lcl|\S+_prot_\S+", line)[0][5:]

            else:
                rang+=1
                nom = re.findall("lcl|\S+_prot_\S+", line)[0][5:]
            len_seq =0

        else:
            len_seq +=len(line)

    D[nom] = [specie, len_seq, rang, 'Uncharacterized protein']
    return D

def readcdsout(fichier, specie1, specie2):
    '''
    Lit un fichier cds.out et remplit un dictionnaire contenant les informations de la table Blast dans la database
    '''
    D={}
    count = 0
    flux = open(fichier)
    for line in flux:
        if line[0]!='#':
            line = line.rstrip().split(None, 12)
            query = line[0][4:]
            subject = line[1]
            couple = (query, subject)
            evalue = float(line[-2])
            identite = float(line[2])
            c_query = float(line[7]) - float(line[6])
            c_subject = float(line[9]) - float(line[8])
            if couple not in D.keys():
                D[couple] = [identite, c_query, c_subject, evalue, specie1, specie2]
    return D

def cover(fichier1, fichier2, fichier3, specie1, specie2):
    '''
    Calcule la couverture des query et des subject
    '''
    Genes1 = readfaa(fichier1, specie1)
    Genes2 = readfaa(fichier2, specie2)
    Blast = readcdsout(fichier3, specie1, specie2)
    for key in Blast:
        key1, key2 = key
        Blast[(key1, key2)][1] /= Genes1[key1][1]
        Blast[(key1, key2)][1] = np.round(Blast[(key1, key2)][1], 3)

        Blast[(key1, key2)][2] /= Genes2[key2][1]
        Blast[(key1, key2)][2] = np.round(Blast[(key1, key2)][2], 3)

    return Genes1, Genes2, Blast

def fillDB(L_genes, L_Blast):
    '''
    Remplit la database à partir des informations données en entrée
    input1 -> liste de dictionnaires créés à partir des fichiers .faa
    input2 -> liste de dictionnaires créés à partir des fichier cds.out
    output -> None
    '''
    conn = psycopg2.connect(database="projetIG")
    cur = conn.cursor()

    for gene in L_genes:
        for key in gene:
            cur.execute("INSERT INTO proteomes (proteine, espece, longueur, rang_prot, fonction) VALUES(%s, %s, %s, %s, %s)", (key, gene[key][0], gene[key][1], gene[key][2], gene[key][3]))
            conn.commit()

    for blast in L_Blast:
        for key in blast:
            cur.execute("INSERT INTO blast (query, subject, evalue, cover_query, cover_subject, identite, espece_query, espece_subject) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (key[0], key[1], blast[key][0], blast[key][1], blast[key][2], blast[key][3], blast[key][4], blast[key][-1]))
            conn.commit()

    cur.close()
    conn.close()
    pass

@njit
def stringence(M, Vfenetre, Vstringence):    
    n, m = M.shape
    for i in range(n):
        for j in range(m):
            SM = 0
            nb = 0
            L = []
            for k in range(Vfenetre):
                if i+k >= len(M) or j+k >= len(M[0]):
                    break
                L.append(M[i+k, j+k])
            nb = len(L)
            for l in L:
                SM += l
            SM = SM / nb
            if float(Vstringence) <= SM:
                M[i, j] = 1
            else:
                M[i, j] = 0
    pass

class dotplot():
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title('DOT PLOT')

        self.barre1 = tk.Label(self.fenetre, text="Couple query-subject")
        self.barre1.grid(row=0, column=0)
        conn = psycopg2.connect(database="projetIG")
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT espece_query, espece_subject FROM blast")
        species1 = cur.fetchall()

        self.species1=[]
        for k in species1:
            self.species1.append(tuple(k))

        self.specie1 = ttk.Combobox(self.fenetre, values=self.species1)
        self.specie1.grid(row=0, column=1)
        self.specie1.config(width=40)
        self.specie1.bind("<<ComboboxSelected>>", self.on_specie1)
        
        self.separator1 = tk.Label(self.fenetre, text='', width=10).grid(row=2, column=0)
        
        self.species = {}
        flux=open("prokaryotes_complete-genomes.csv")
        for line in flux:
            if line[0]!='#':
                line = line.rstrip().split(',', 15)
                genre = re.findall("^\".+\S+", line[0])[0][1:2] + '.'
                espece = re.findall(" \S+", line[0])[0][:-1]
                strain = ' ' + line[2][1:-1]
                link = line[-1][1:-1]
                self.species[genre + espece + strain] = link
        
        self.lesnoms = []
        for key in self.species:
            self.lesnoms.append(key)

        self.barrespecie = tk.Label(self.fenetre, text="Ajout query-subject :")
        self.barrespecie.grid(row=3, column=0)

        self.ajoutquery = ttk.Combobox(self.fenetre, value=self.lesnoms)
        self.ajoutquery.grid(row = 3, column = 1)
        self.ajoutquery.bind("<<ComboboxSelected>>", self.add_specie)

        self.ajoutsubject = ttk.Combobox(self.fenetre, value=self.lesnoms)
        self.ajoutsubject.grid(row = 3, column = 2)
        self.ajoutsubject.bind("<<ComboboxSelected>>", self.add_specie)
        self.separator2 = tk.Label(self.fenetre, text='', width=10).grid(row=4, column=0)

        self.ajoutbut = tk.Button(self.fenetre, text="ADD COUPLE", command=self.add_couple)
        self.ajoutbut.grid(row=4, column = 1)
        
        self.separator3 = tk.Label(self.fenetre, text='', width=10).grid(row=5, column=0)

        self.ident = tk.BooleanVar(value=False)
        self.identbut = tk.Checkbutton(self.fenetre, text='Pourcentage d\' identité', variable=self.ident, offvalue=False, onvalue=True)
        self.identbut.grid(row=6, column=0, sticky="w")
        self.seuilident = tk.Entry(self.fenetre)
        self.seuilident.grid(row=6, column=2)
        self.labident = tk.Label(self.fenetre, text='Seuil identité :')
        self.labident.grid(row=6, column=1, sticky="e")

        self.evalue = tk.BooleanVar(value=False)
        self.evaluebut = tk.Checkbutton(self.fenetre, text='E-value', variable=self.evalue, offvalue=False, onvalue=True)
        self.evaluebut.grid(row=7, column=0, sticky="w")
        self.seuilevalue = tk.Entry(self.fenetre)
        self.seuilevalue.grid(row=7, column=2)
        self.labevalue = tk.Label(self.fenetre, text='Seuil e-value :')
        self.labevalue.grid(row=7, column=1, sticky="e")
        
        self.cover = tk.BooleanVar(value=False)
        self.coverbut = tk.Checkbutton(self.fenetre, text='Couverture du hit', variable=self.cover, offvalue=False, onvalue=True)
        self.coverbut.grid(row=8, column=0, sticky="w")
        self.seuilcover1 = tk.Entry(self.fenetre)
        self.seuilcover1.grid(row=8, column=2)
        self.labelcover1 = tk.Label(self.fenetre, text='Seuil cover query :')
        self.labelcover1.grid(row=8, column=1, sticky="e")
        self.seuilcover2 = tk.Entry(self.fenetre)
        self.seuilcover2.grid(row=9, column=2)
        self.labelcover2 = tk.Label(self.fenetre, text='Seuil cover subject :')
        self.labelcover2.grid(row=9, column=1, sticky="e")

        self.annotation = tk.BooleanVar(value=False)
        self.annotationbut = tk.Checkbutton(self.fenetre, text='Annotation fonctionnelle (en dev)', variable=self.annotation, offvalue=False, onvalue=True)
        self.annotationbut.grid(row=10, column=0, sticky="w")
        self.seuilannotation = tk.Entry(self.fenetre)
        self.seuilannotation.grid(row=10, column=2)
        self.labannotation = tk.Label(self.fenetre, text='Seuil evalue annot :')
        self.labannotation.grid(row=10, column=1, sticky="e")

        self.separator3 = tk.Label(self.fenetre, text='', width=10).grid(row=11, column=0)

        self.taillefenetre = tk.Entry(self.fenetre)
        self.taillefenetre.grid(row=12, column = 1)
        self.labtaillefenetre = tk.Label(self.fenetre, text='Taille de la fenêtre :')
        self.labtaillefenetre.grid(row=12, column=0, sticky="e")

        self.seuilstringence = tk.Entry(self.fenetre)
        self.seuilstringence.grid(row=13, column=1)
        self.labtaillefenetre = tk.Label(self.fenetre, text='Seuil de stringence :')
        self.labtaillefenetre.grid(row=13, column=0, sticky="e")

        self.separator4 = tk.Label(self.fenetre, text='', width=10).grid(row=13, column=0)

        self.bouton = tk.Button(self.fenetre, text="DRAW", command=self.Exec)
        self.bouton.grid(row=14, column = 1)
        self.fenetre.mainloop()
        cur.close()
        conn.close()

    def add_specie(self, event):
        self.new_query = self.ajoutquery.get()
        self.new_subject = self.ajoutsubject.get()
        pass

    def add_couple(self):
        texte = (self.new_query, self.new_subject)
        if texte in self.species1:
            print('Ce couple existe déjà !')
        else:
            lien = self.species[self.new_query]
            lien2 = self.species[self.new_subject]
            
            # Connexion au serveur FTP
            ftp = FTP('ftp.ncbi.nlm.nih.gov')
            ftp.login()

            # Naviguer vers le répertoire approprié
            ftp.cwd(lien[26:])

            # Liste des fichiers dans le répertoire
            files = ftp.nlst()

            # Télécharger le fichier .faa
            for file in files:
                if file.endswith('_cds.faa.gz'):
                    with open(file, 'wb') as f:
                        ftp.retrbinary('RETR '+ file, f.write)
                        break

            # Fermer la connexion FTP
            ftp.quit()

            # Décompression du fichier .faa.gz et enregistrement du contenu dans un fichier texte
            filename1 = file[:-21] + 'protein.faa'
            with gzip.open(file, 'rb') as f_in:
                with open(filename1, 'w') as f_out:
                    f_out.write(f_in.read().decode('utf-8'))

            # Suppression du fichier .faa.gz
            os.remove(file)

            ftp = FTP('ftp.ncbi.nlm.nih.gov')
            ftp.login()

            ftp.cwd(lien2[26:])

            files = ftp.nlst()

            for file in files:
                if file.endswith('_cds.faa.gz'):
                    with open(file, 'wb') as f:
                        ftp.retrbinary('RETR '+ file, f.write)
                        break

            ftp.quit()

            filename2 = file[:-21] + 'protein.faa'
            with gzip.open(file, 'rb') as f_in:
                with open(filename2, 'w') as f_out:
                    f_out.write(f_in.read().decode('utf-8'))

            os.remove(file)

            query_file = filename1
            subject_file = filename2

            out_file = "QUERY-" + filename1[:-4] + "__DB-" + filename2[:-4] + ".out"

            command = ["makeblastdb", "-in", subject_file, "-out", "DB", "-dbtype", "prot", "-parse_seqids"]
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            cmd = ["blastp", "-query", query_file, "-db", "DB", "-out", out_file, "-outfmt", "6 qseqid sseqid pident length mismatch gaps qstart qend sstart send evalue bitscore"]

            # Exécute la commande et stocke la sortie et les erreurs
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            query, subject, blast = cover(query_file, subject_file, out_file, self.new_query, self.new_subject)
            L_genes = [query, subject]
            L_Blast = [blast]
            fillDB(L_genes, L_Blast)
            
            os.remove(query_file)
            os.remove(subject_file)
            os.remove(out_file)
            files = glob.glob("DB*")
            for file in files:
                os.remove(file)

            print("L'ajout a bien été réalisé")
        pass

    def on_specie1(self, event):
        self.espece_query = re.findall("{(.+?)}",self.specie1.get())[0]
        self.espece_subject = re.findall("{(.+?)}",self.specie1.get())[1]
        pass
    
    def Exec(self):
            self.Vident = self.ident.get()
            self.Vsident = self.seuilident.get()

            self.Vevalue = self.evalue.get()
            self.Vsevalue = self.seuilevalue.get()

            self.Vcover = self.cover.get()
            self.Vscover1 = self.seuilcover1.get()
            self.Vscover2 = self.seuilcover2.get()

            self.Vannotation = self.annotation.get()
            self.Vsannotation = self.seuilannotation.get()

            self.Vfenetre = self.taillefenetre.get()

            self.Vstringence = self.seuilstringence.get()

            self.criteres = [self.Vevalue, self.Vcover, self.Vcover, self.Vident]
            seuils = [self.Vsevalue ,self.Vscover1, self.Vscover2, self.Vsident]
            self.seuil=[]

            for i in range(len(self.criteres)):
                if self.criteres[i]:
                    self.seuil.append(float(seuils[i]))
                else:
                    if i!=0:
                        self.seuil.append(-1)
                    else:
                        self.seuil.append(100) 
            
            conn = psycopg2.connect(database="projetIG")
            cur = conn.cursor()

            cur.execute("SELECT * FROM blast WHERE espece_query = %s AND espece_subject = %s", (self.espece_query, self.espece_subject))
            self.results = cur.fetchall()

            self.liste = []
            for prot in self.results:
                rang_query = int(re.findall("_\d+", prot[0])[-1][1:])
                rang_subject = int(re.findall("_\d+", prot[1])[-1][1:])
                self.liste.append([rang_query, rang_subject, prot[2], prot[3], prot[4], prot[5]])
            
            cur.execute("SELECT * FROM proteomes WHERE espece = %s", (self.espece_query,))
            n = len(cur.fetchall())

            cur.execute("SELECT * FROM proteomes WHERE espece = %s", (self.espece_subject,))
            m = len(cur.fetchall())

            self.matrix = np.zeros((n, m))
            for element in self.liste:
                i = element[0]
                j = element[1]
                self.matrix[i-1, j-1] = 1
                for k in range(len(element)- 2):
                    if element[k+2] <= self.seuil[k] and k!=0:
                        self.matrix[i-1, j-1] = 0
                    elif element[k+2] >= self.seuil[k] and k==0:
                        self.matrix[i-1, j-1] = 0
                        break
            
            if self.Vfenetre and self.Vstringence:
                self.Vfenetre = int(self.Vfenetre)
                self.Vstringence = float(self.Vstringence)
                stringence(self.matrix, self.Vfenetre, self.Vstringence)

            plt.imshow(self.matrix, cmap='gray')
            plt.show()
            cur.close()
            conn.close()
            pass

D = dotplot()