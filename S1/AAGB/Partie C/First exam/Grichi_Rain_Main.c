#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "Rain.h"


int main(){
    //fonctions de la Partie 1
    tyCase t[6] ={{1,0},{2,0},{1,0},{1,0},{3,0},{2,0}};
    int total_eau=sommeTab(t,6);
    printf("QUESTION 2 -> Quantité d'eau stockée : %d\n",total_eau);

    int max_barre=maximumBarreTab(t,6);
    printf("QUESTION 3 -> Plus grande barre en : %d\n",max_barre);

    fillWater(t,6);
    total_eau=sommeTab(t,6);
    printf("QUESTION 4 -> Quantité d'eau stockée : %d\n",total_eau);

    //afficheRainWatter(t,6); //QUESTION 5

    //fonctions de la Partie 2
    int nb_lignes=compter_lignes("unTab.txt");
    printf("QUESTION 7 -> Le nombre de barres dans le fichier est : %d\n",nb_lignes);

    int p_nbVal=0;
    tyCase *tab=lire_tableau("unTab.txt", &p_nbVal);
    printf("QUESTION 8 -> Nombre de barre dans le nvx tyCase %d\n",p_nbVal); //juste pour vérifier que p_nbVal est bien modifié
    
    /* QUESTION 9 : 
    afficheRainWatter(tab,p_nbVal);
    fillWater(tab,p_nbVal);
    afficheRainWatter(tab,p_nbVal);*/
    return 0;
}