#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ManipSeqADN.h"
#include "ManipSeqSimple.h"


/*Allocation et desallocation*/
tySeqADN *newSeqADN(){
	tySeqADN *pA = malloc(sizeof(tySeqADN));
	pA -> seq = NULL;
	pA -> lg = 0;
	pA -> GC = -1;
	return pA;}

void freeSeqADN(tySeqADN *pS){
	FreeSeq(pS->seq);
	free(pS);}

/*Création du brin complémentaire*/
tySeqADN *complementaire(tySeqADN *pS){
	tySeqADN *pA = malloc(sizeof(tySeqADN));
	pA -> seq =BrinComplementaire(pS->seq, pS->lg);
	pA -> lg = pS -> lg;
	pA -> GC = pS -> GC;
	return pA;}




/*Lecture de fichier au format .fasta*/
int CompterNbSeq(char *nomFi){
	char Ligne[1000]="";int n_sqce=0;	//on initialise une chaine de caractère vide qui fait la taille de 10k caractères
	FILE *pFi = NULL;					//on initialise le pointeur pFi qui est un pointeur d'un fichier de type FILE (un fichier en somme)
	pFi=fopen(nomFi,"r");
	if(pFi==NULL){
		fprintf(stderr,"Ne peut ouvrir %s\n",nomFi);	//stderr donne une standard error
		exit(1);}
	while(fgets(Ligne,1000,pFi)!=NULL){
		if(Ligne[0]=='>')
			n_sqce++;}
	fclose(pFi);
	return n_sqce;}

tySeqADN *LireUneSeqFasta(FILE *pFi){
	tySeqADN *pS = NewSeqADN();
	char Ligne[1000];
	int SeqLine=0;
	pS -> seq[0] = '\0';
	while(fgets(Ligne,1000,pFi)!=NULL){
		if(Ligne[0]!='>'){
			pS -> lg += lg-1
			pS -> seq = realloc(pS -> seq,(pS -> lg-1)*sizeof(char));
			//continuer à la maison
		}
	}
		return pS;}
	while(fgets(Ligne))
}