#TP Interface Graphique

import tkinter as tk

class fenetre():
    def __init__(self):
        self.fenetre = tk.Tk()                              #crée la fenêtre
        self.fenetre.title('Flèches directionnelles')       #la nomme
        self.panG = tk.PanedWindow(self.fenetre)            #crée un sous espace de l'interface où on va pouvoir y mettre des choses
        self.LabG = tk.Label(self.panG, text='Vertical')      #attribut un nom au sous espace crée
        self.LabG.pack()                                    #positionne dans la fenêtre (tant que cet objet n'est pas packé il existe mais n'est pas affiché)
        self.boutH = tk.Button(self.panG, text = 'Haut')    #crée un bouton dans un sous espace de l'interface (au choix)
        self.boutH.pack(side=tk.TOP)                        #positionne le bouton en haut du sous espace 
        self.boutB = tk.Button(self.panG, text = 'Bas')
        self.boutB.pack(side=tk.BOTTOM)

        self.panD = tk.PanedWindow(self.fenetre)
        self.LabD = tk.Label(self.panD, text='Horizontal')
        self.LabD.pack()
        self.boutD = tk.Button(self.panG, text = 'Droit')
        self.boutD.pack(side=tk.RIGHT)
        self.boutG = tk.Button(self.panG, text = 'Gauche')
        self.boutG.pack(side=tk.LEFT)
        
        self.panG.pack(side = tk.LEFT)                      #place le panneau à gauche de l'interface
        self.panD.pack(side = tk.RIGHT)
        self.fenetre.mainloop()                             #crée la fenêtre

#H = fenetre()

class Grille():
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title('Points cardinaux')
        self.PanN = tk.PanedWindow(self.fenetre)
        self.boutNW = tk.Button(self.PanN,text="NW")
        self.boutNE = tk.Button(self.PanN,text="NE")
        self.boutNW.pack(side=tk.LEFT)
        self.boutNE.pack(side=tk.RIGHT)
        self.PanS = tk.PanedWindow(self.fenetre)
        self.boutSW = tk.Button(self.PanS,text="SW")
        self.boutSE = tk.Button(self.PanS,text="SE")
        self.boutSW.pack(side=tk.LEFT)
        self.boutSE.pack(side=tk.RIGHT)
        self.PanN.pack(side=tk.TOP)                        #permet de dire que on met le panneau PanN en haut -> donc on aura NW et NE placés en haut à droite/gauche
        self.PanS.pack(side=tk.BOTTOM)                     #même chose ici sauf que ça sera en bas à droite/gauche
        self.fenetre.mainloop()

#G = Grille()


class Dessin():
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title('Dessin')
        # Cree et positionne le Canvas
        self.tableau = tk.Canvas(self.fenetre)            #permet de créer un canva -> càd un truc sur lequel on peut dessiner
        self.tableau.pack()
        # Dessine sur le Canvas
        self.tableau.create_oval(150, 100, 370, 260)      #on crée un ovale avec les caractéristique qu'on veut
        self.tableau.create_rectangle(80,60,240,200)
        self.tableau.create_line(40,240,270,50)
        self.tableau.create_text(300,40,text="Coucou")   #on écrit à un certain endroit
        self.fenetre.mainloop()

#D = Dessin()


class MenuApp():
    def __init__(self):
        self.fichier = ''
        self.fenetre = tk.Tk()
        self.barre = tk.Menu(self.fenetre)
        self.filemenu = tk.Menu(self.barre,tearoff=0)
        self.filemenu.add_command(label="New",
        command=self.rien)
        self.filemenu.add_command(label="Open...",command=self.ouvrir)      #commande qui est executé si on clique sur "Open"
        self.filemenu.add_command(label="Save", command=self.rien)
        self.barre.add_cascade(label="File", menu=self.filemenu)
        self.fenetre.config(menu=self.barre)
        self.fenetre.mainloop()

        def rien(self):
            print("OK")
        
        def ouvrir(self):                                                  #et en l'occurence la commande exécuté est une méthode
            self.fenetre.withdraw()
            self.fichier = fd.askopenfilename()
            self.fenetre.deiconify()
            print(self.fichier)

#M = MenuApp()