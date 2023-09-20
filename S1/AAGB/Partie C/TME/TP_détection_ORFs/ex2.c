/* Nous souhaitons calculer l'indice a partir duquel la somme des elements d'un tableau atteint une borne donnee.
Exemple:
tab={4,5,8,1,9,5}, Borne=15, l'indice est 2 car (4+5+8=17 (>borne) et 4+5=9 (< borne))

- Completez la fonction indSomme pour qu'elle retourne l'indice a partir duquel la somme des elements 
  d'un tableau atteint une borne donnee. 
  La fonction doit prendre en parametres le tableau, sa taille et la borne.
  La fonction doit retourner -1 si la borne n'est jamais atteinte.

- Completez la fonction main pour afficher le resultat. Le message affiche doit dependre du resultat de l'appel
  a la fonction indSomme. N'oubliez pas de remplacer les ... en parametre des appels a printf.

Les elements du tableau, sa taille et la borne sont definis par des primitives #define, ces valeurs seront modifiees pour tester votre programme. Vous pouvez les modifier pour effectuer des tests.
*/

#include <stdio.h>


... indSomme(...) {
 
}

int main ()
{
  int borne= 15;
  int tab[6]={4,5,8,1,9,5};
   
  printf("La borne est atteinte a l'indice %d\n",...);
 
  printf("La borne n'est jamais atteinte\n");
  
  return 0;
}
