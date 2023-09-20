#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "Rain.h"

//Question 2
int sommeTab(tyCase tab[], int n){
	int total_eau=0;
	int k;
	for(k=0;k<n-1;k++){
		total_eau+=tab[k].eau;}
	return total_eau;}

//Question 3
int maximumBarreTab(tyCase tab[], int n){
	int k;
	int max=0;
	int i;
	for(k=0;k<n;k++){
		if(max<tab[k].barre){
			max=tab[k].barre;
			i=k;}}
	return i;}

//Question 4

void fillWater(tyCase tab[], int n){
	int k;
	int max = maximumBarreTab(tab,n);
	int max_local = 0;
	for(k=0;k<max;k++){
		if(max_local<tab[k].barre){
			max_local=tab[k].barre;}
		tab[k].eau=max_local;}
	max_local=0;
	for(k=n-2;k>=max;k--){
		if(max_local<tab[k+1].barre){
			max_local=tab[k+1].barre;}
		tab[k].eau=max_local;}}


//Question 5

/*void afficheRainWatter(tyCase *tab, int n){
	int i = maximumBarreTab(tab,n);
	int barre_max = tab[i].barre
	FILE *pFi;
	pFi=fopen("afficheRain.txt","w");
	int k;
	for(k=0;k<barre_max;k++){
		Ligne[k+1]=...
	}
}*/
//L'idée de cette fonction était de créer un fichier qui écrit


//Question 7
int compter_lignes(char *nomFichier){
	FILE *pFi;
	char Ligne[10];
	pFi=fopen(nomFichier,"r");
	int nb_lignes=0;
	if(pFi==NULL){
		printf("Erreur dans l'ouverture du fichier\n");
		return 0;}
	while(fgets(Ligne,10,pFi)!=NULL){
		nb_lignes++;}
	return nb_lignes;}

//Question 8
tyCase *lire_tableau(char *nomFichier, int *p_nbVal){
	int nb_lignes=compter_lignes(nomFichier);
	*p_nbVal=nb_lignes;
	tyCase *tab = malloc(sizeof(tyCase)*nb_lignes);
	FILE *pFi;
	int k=0;
	char Ligne[10];
	pFi=fopen(nomFichier,"r");
	if(pFi==NULL){
		printf("Erreur dans l'ouverture du fichier\n");
		exit(1);}
	while(fgets(Ligne,10,pFi)!=NULL){
		tab[k].barre=Ligne[0];
		tab[k].eau=0;
		k++;}
	return tab;
}


