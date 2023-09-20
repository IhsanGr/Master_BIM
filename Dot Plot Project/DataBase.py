import psycopg2
import re
import numpy as np

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

def readout(fichier):
    D={}
    flux = open(fichier)
    for line in flux:
        if line[0:2] == 'Q#':
            line = line.rstrip()
            nom = re.findall(">lcl|\S+", line)[3][1:]
            cog = re.findall("COG\S+", line)
            if cog!=[]:
                D[nom] = cog[0]

    return D

def cogtxt(fichier):
    D={}
    flux = open(fichier)
    for line in flux:
        line = line.rstrip()
        if line[0] == 'C':
            cog = re.findall("C\S+", line)[0]
            fonction = re.findall("\t.+", line)[0][3:]
            D[cog] = fonction

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

def func(D_gene, D_out, D_cog):

    for key in D_out:
        if key in D_gene:
            D_gene[key][-1] = D_cog[D_out[key]]

    return D_gene

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



D_cog = cogtxt('cognames2003-2014.tab.txt')

Genes1, Genes2, Blast12 = cover('GCA_000014865.1_ASM1486v1_translated_cds.faa', 'GCA_000009985.1_ASM998v1_translated_cds.faa', 'QUERY-GCA_000014865.1_ASM1486v1_translated_cds__DB-GCA_000009985.1_ASM998v1_translated_cds.out', 'M. marinus MC-1', 'M. magneticum AMB-1')
Genes1_func = readout('QUERY-GCA_000014865.1_ASM1486v1_translated_cds__DB-COGv3-16.out')
Genes1 = func(Genes1, Genes1_func, D_cog)
Genes2_func = readout('QUERY-GCA_000009985.1_ASM998v1_translated_cds__DB-COGv3-16.out')
Genes2 = func(Genes2, Genes2_func, D_cog)

Genes3, Genes4, Blast34 = cover('GCA_001580455.1_ASM158045v1_translated_cds.faa', 'GCA_000215705.1_ASM21570v1_translated_cds.faa', 'QUERY-GCA_001580455.1_ASM158045v1_translated_cds__DB-GCA_000215705.1_ASM21570v1_translated_cds.out', 'R. tataouinensis', 'R. tataouinensis TTB310')
Genes3_func = readout('QUERY-GCA_001580455.1_ASM158045v1_translated_cds__DB-COGv3-16.out')
Genes3 = func(Genes3, Genes3_func, D_cog)
Genes4_func = readout('QUERY-GCA_000215705.1_ASM21570v1_translated_cds__DB-COGv3-16.out')
Genes4 = func(Genes4, Genes4_func, D_cog)

Genes5, Genes6, Blast56 = cover('GCA_002843685.1_ASM284368v1_translated_cds.faa', 'GCA_000026265.1_ASM2626v1_translated_cds.faa', 'QUERY-GCA_002843685.1_ASM284368v1_translated_cds__DB-GCA_000026265.1_ASM2626v1_translated_cds.out', 'E. coli K-12', 'E. coli IAI1')
Genes5_func = readout('QUERY-GCA_002843685.1_ASM284368v1_translated_cds__DB-COGv3-16.out')
Genes5 = func(Genes5, Genes5_func, D_cog)
Genes6_func = readout('QUERY-GCA_000026265.1_ASM2626v1_translated_cds__DB-COGv3-16.out')
Genes6 = func(Genes6, Genes6_func, D_cog)

L_genes = [Genes1, Genes2, Genes3, Genes4, Genes5, Genes6]
L_Blast = [Blast12, Blast34, Blast56]

fillDB(L_genes, L_Blast)
