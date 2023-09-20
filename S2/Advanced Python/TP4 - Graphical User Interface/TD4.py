#TD4 Python_avance

import tkinter as tk
from tkinter import filedialog as fd
import re


class fenetre():
    def __init__(self):
        self.fichier = fd.askopenfilename()
        self.extraireAllFastaMulti()


        self.fenetre = tk.Tk()
        self.fenetre.title('Motifs')
        self.Pan = tk.PanedWindow(self.fenetre)
        self.Lab = tk.Label(self.Pan, text='Motifs :')
        self.Lab.pack(side = tk.LEFT)
        self.barre_recherche = tk.Entry(self.Pan)
        self.barre_recherche.pack(side = tk.TOP)
        self.Pan.pack(side = tk.TOP)

        self.barre = tk.Menu(self.fenetre)
        self.filemenu = tk.Menu(self.barre,tearoff=0)
        self.filemenu.add_command(label="Open", command=self.ouvrir)
        self.filemenu.add_command(label="Save", command=self.save)
        self.barre.add_cascade(label="File", menu=self.filemenu)
        self.fenetre.config(menu=self.barre)

        self.seqmenu = tk.Menu(self.barre,tearoff=0)
        for s in self.nomSeqs:
            self.seqmenu.add_command(label=s, command = self.choose)
        self.barre.add_cascade(label="Séquences", menu=self.seqmenu)
        self.fenetre.config(menu=self.barre)

        self.Pan2 = tk.PanedWindow(self.fenetre)
        self.boutC = tk.Button(self.Pan2, text = 'Chercher', command=self.search)
        self.boutC.pack(side = tk.TOP)

        self.inv = tk.IntVar(value=0)
        self.invbut = tk.Checkbutton(self.Pan2, text='Inverses-complémentaire', variable=self.inv, offvalue=0, onvalue=1)
        self.invbut.pack(side = tk.BOTTOM)

        self.Pan2.pack(side = tk.BOTTOM)
        self.fenetre.mainloop()

    def ouvrir(self):
        self.fenetre.withdraw()
        self.fichier = fd.askopenfilename()
        self.fenetre.deiconify()
    
    def save(self):
        print('pass')

    def choose(self):
        print('pass')

    def extraireAllFastaMulti(self):
        self.Seqs = []
        self.nomSeqs = []
        seq = ''
        
        flux = open(self.fichier)
        for line in flux :
            line = line.rstrip()
            
            
            if line[0] == '>':
                self.nomSeqs.append(line[1:])
                if seq!= '':
                    self.Seqs.append(seq)
                seq = ''

            else:
                seq+=line[:]
                
        self.Seqs.append(seq)
        self.lenSeqs = len(self.Seqs)
        self.tailleSeq = len(self.Seqs[0])



    def complementaire(self):
        Dico = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
        self.Seqs_comp = []
        seq = ''
        for k in range(self.tailleSeq):
            seq+=Dico[self.Seqs[0][self.lenSeqs - k - 1]]
        self.Seqs_comp.append(seq)

    def search(self):
        state = self.inv.get()
        self.motif = self.barre_recherche.get()
        q = len(self.motif)
        n = self.tailleSeq
        if state == 0:
            for s in range(self.lenSeqs):
                for k in range(n-q):
                    if self.motif in self.Seqs[0][k:k+q]:
                        print(self.nomSeqs[s] + ' :' + str(k+1) + ' - ' + str(k+q))

        else:
            self.complementaire()
            for s in range(self.lenSeqs):
                for k in range(n-q):
                    if self.motif in self.Seqs_comp[s][k:k+q]:
                        print(self.nomSeqs[s] + ' :'  + str(k+1) + ' - ' + str(k+q))

f = fenetre()