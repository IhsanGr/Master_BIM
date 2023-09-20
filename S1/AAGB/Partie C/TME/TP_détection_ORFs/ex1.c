/* Ce programme calcule la valeur de la constante d'Euler e
   avec une erreur relative inferieure a ERREUR */

#include <stdio.h>
#define ERREUR 0.0001

float euler(float err) {
  int k = 0;
  float e = 0.0, old_e, terme = 1.0;
  
  do {
     old_e = e;
     e = e + terme;
     k++;
     terme = terme * 1.0/k;
  } while ( (e - old_e)/e > err)
  
    return e;
}

main() {
   printf("e = %d\n", euler(ERREUR,100));
   return 0 ;
}
