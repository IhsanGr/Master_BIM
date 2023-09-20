#include <stdlib.h> 
#include <stdio.h> 
#include  <string.h> 

typedef struct {
    char *seq;
    int lg;
    float GC;
    float GC1;
    float GC2;
    float GC3;
} tySeqADN;

void InitSeqAlea(char seq[], int lg);
void AfficheSeq(char seq[], int lg);
tySeqADN* TabSeqAlea(int nbSeq);
void CompterSeqEtLgMax(char *nomFi, int *pNbSeq, int *pLgSeq);
tySeqADN *readFasta(char *nomFi, int *pNbSeq);
void GC(tySeqADN  *seqADN);
void BiasGC(tySeqADN  seqADN[], int nbSeq, char *nomFi);



void InitSeqAlea(char seq[], int lg){
 

 }


void AfficheSeq(char seq[], int lg){

}


tySeqADN* TabSeqAlea(int nbSeq){
 return NULL;
}



void GC(tySeqADN  *seqADN){

	int i;
 
}

void BiasGC(tySeqADN  tSeq[], int nbSeq, char *nomFi){

}

void CompterSeqEtLgMax(char *nomFi, int *pNbSeq, int *pLgMaxSeq){
 
}

tySeqADN *readFasta(char *nomFi, int *pNbSeq){
 return NULL;
 
}



int main(){

 
    return 0;
}

