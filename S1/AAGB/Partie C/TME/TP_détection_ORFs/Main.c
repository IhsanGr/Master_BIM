#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "ManipSeqADN.h"
#include "ManipSeqSimple.h"


/************************************/
int main(int argc, char *argv[]){
    tySeqADN *pS, *pComp;//, *pS2;
    pS=newSeqADN();
    pS->seq = NewSeq(12);
    pS->lg = 12;
    InitSeqAlea(pS->seq,pS->lg);
    pComp=complementaire(pS);
    AfficheSeq(pS->seq,pS->lg);
    AfficheSeq(pComp->seq,pComp->lg);
    freeSeqADN(pS);
    freeSeqADN(pComp);
    int n_sqce=CompterNbSeq("NC_000964.ffn");
    printf("Nb de sqces dans le fichier : %d\n",n_sqce);
    return 0;}