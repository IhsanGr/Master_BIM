#TP1 POO
import random as rd

#Exercice 1 : cercles, cylindre et cône

#1/
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return self.rayon * 5

#2/
class Cylindre(Cercle):
    def __init__ (self, rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur

#3/ 
class Cone(Cylindre):
    def __init__(self, rayon, hauteur):
        Cylindre.__init__(self,rayon, hauteur)

    def volume_c(self):
        return self.volume() / 3
    
#Exercice 2

#1/
class JeuDeCartes:
    def __init__(self):
        Cartes = []
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'reine', 'roi', 'as']
        type = ['coeur', 'trefle', 'pique', 'carreau']
        for v in type :
            for t in valeurs:
                Cartes.append((t, v))
        self.cartes = Cartes


    def nom_carte(self, carte):
        return(carte[0] + ' de ' + carte[1])
    
    def battre(self):
        rd.shuffle(self.cartes)
    
    def tirer(self):
        if self.cartes == []:
            return None
        else :
            carte = self.cartes[0]
            self.cartes = self.cartes[1:]
            return carte

#2/
def main():
    '''rayon = 5

    Objet = Cercle(rayon)
    print('Surface du cercle', Objet.surface())

    hauteur = 10

    Objet = Cylindre(rayon, hauteur)
    print('Volume du cylindre', Objet.volume())

    Objet = Cone(rayon, hauteur)
    print('Volume du cône', Objet.volume_c())'''

    jeu = JeuDeCartes()
    jeu.battre()
    for n in range(53):
        c = jeu.tirer()
        if c == None:
            print("Terminé !")
        else:
            print(jeu.nom_carte(c))

    j1 = JeuDeCartes()
    j2 = JeuDeCartes()
    j1.battre()
    j2.battre()

    sj1 = 0
    sj2 = 0

    for n in range(52):
        c1 = j1.tirer()
        c2 = j2.tirer()
        v1 = c1[0]
        v2 = c2[0]

        if c1 == 'valet':
            v1 = 11
        elif c1 == 'reine' :
            v1 = 12
        elif c1 == 'roi' :
            v1 = 13
        elif c1 == 'as' :
            v1 = 14

        if c2 == 'valet':
            v2 = 11
        elif c2 == 'reine' :
            v2 = 12
        elif c2 == 'roi' :
            v2 = 13
        elif c2 == 'as' :
            v2 = 14

        if v1 > v2:
            print(j1.nom_carte(c1), ' VS ', j2.nom_carte(c2), '=> j1 gagne')
            sj1+=1
        elif v1 < v2:
            print(j1.nom_carte(c1), ' VS ', j2.nom_carte(c2), '=> j2 gagne')
            sj2+=1
    
    if sj1 < sj2:
        print('j1 remporte la partie')
    
    elif sj2 < sj1 :
        print('j2 remporte la partie')

main()
