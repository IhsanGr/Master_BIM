#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "ManipSeqADN.h"
#include "ManipSeqSimple.h"

typedef struct _tyArbre{
    struct _tyArbre *pFG,*pFD; //fils gauche et droit
    char *seq; //pointeur vers le début de la graine
    int nbcodons; // nombre de codons dans l'ORF
    //int complementaire; 0 si c'est sur le brin et 1 si c'est sur le brin complémentaire
}tyArbre;

//Trouver les graines d'une séquence
char **Trouver_seed(char *seq, int taille_seed){
    int n = strlen(seq);
    int i;
    char **tab;
    int taille_tab = 1;
    char mot[taille_seed+1];
    tab = malloc(sizeof(char*));
    tab[0] = malloc(sizeof(char)*taille_seed+1);
    for(i=0;i<n-taille_seed+1;i++){
        int k;
        for(k=i;k<taille_seed+i;k++){
            mot[k-i] = *(seq + k);}
        mot[taille_seed+1] = '\0';
        tab = realloc(tab, sizeof(char*)*taille_tab+1);
        tab[taille_tab-1] = malloc(sizeof(char)*taille_seed+1);
        tab[taille_tab-1] = mot;
        taille_tab++;}
    return tab;}

//Construction de l'arbre des graines (trié par ordre alphabétique)
tyArbre *Ajouter_graine(tyArbre *pA, char *seq, int taille_seed, char **tab, int *compteur){
    char *seed = tab[*compteur];
    tyArbre *pNew = NULL;
    if(pA==NULL){
        pNew = malloc(sizeof(tyArbre));
        pNew->seq = malloc(sizeof(char)*taille_seed);
        pNew->pFG = NULL;
        pNew->pFD = NULL;
        pNew->seq = seed;
        pNew->nbcodons = taille_seed;
        *compteur+=1;
        return pNew;}
    int c = strcmp(seed,pA->seq);
    if(c<0)
        pA->pFG = Ajouter_graine(pA->pFG, seq, taille_seed, tab, compteur);
    if(c>0) //comme ça on ne prend pas en compte les répétitions des graines dans le tableau
        pA->pFD = Ajouter_graine(pA->pFG, seq, taille_seed, tab, compteur);
    return pA;}

//Compte le nombre d'occurences d'une graine donnée
int Occurences_seed(char *seed, char **tab){
    int k;
    int occurence;
    for(k=0;k<strlen(*tab);k++){     //cette fonction ne marche pas à cause du strlen(tab) et je ne comprends pas comment obtenir la taille du tableau autremenent
        if(seed==tab[k])
            occurence++;}
    return occurence;}

//Ecris dans un fichier toutes les graines présentes et leur occurence
void Create_file(tyArbre *pA, FILE *pFi, char** tab){
    if(pA==NULL){
        printf("L'arbre est vide");
        exit(1);
        return;}
    if(pFi!=NULL){
        fprintf(pFi, "Graine : %s \t \t \t \t Nombre d'occurences : %d\n", pA->seq, Occurences_seed(pA->seq, tab));
    }
    Create_file(pA->pFD, pFi, tab);
    Create_file(pA->pFG, pFi, tab);}


//Libération en mémoire de l'arbre des graines
void Detruire_Seed_tree(tyArbre *pA){

    if(pA==NULL)
        return;
    Detruire_Seed_tree(pA->pFG);
    Detruire_Seed_tree(pA->pFD);
    free(pA);
}

//Il y a des problèmes de compatibilité car tout cela a été fait à la fin
int main(){
    //Ce sont les test réalisés :
    char *seq_t;
    seq_t = malloc(sizeof(char)*6);
    seq_t = "ATGATG";

    int k =0;
    char **tab = Trouver_seed(seq_t, 3);
    printf("La graine numéro %d de la sequence %s", k, tab[k]);
    //fin des tests

    int taille_seed = 3; //le plus logique et ce à quoi on peut s'attendre
    tySeqADN *seq = LireFastaSimple("NC_020075.ffn");
    int compteur = 0;
    tyArbre *pA = NULL;
    pA = Ajouter_graine(pA, seq, taille_seed, tab, compteur);
    FILE * pFi;
    pFi = fopen("Seed_occurences.txt","w");
    fclose(pFi);
    char **liste_seq = LireFastaMul("NC_020075.ffn")
    free(liste_seq);
    Detruire_Seed_tree(pA);
    return 0;
}