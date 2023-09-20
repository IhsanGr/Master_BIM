#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>


char *NewSeq(int lg){                               //on met un * avt la fonction pr préciser qu'elle renvoie un pointeur
    char *seq=malloc(lg*sizeof(char));              //on définit sur le pointeur
    return seq;}                                    //on retourne le tableau

char *ReallocSeq(char *seq, int lg){
    char *seq2=realloc(seq,lg*sizeof(char));
    return seq2;}

void FreeSeq(char *seq){
    free(seq);}
    
void InitSeqAlea(char seq[], int lg){
    char Nt;
    int k;
    for(k=0;k<lg;k+=1){
        int rd=rand()%4;
        switch(rd){                           //utiliser srand(time=NULL) dans le main
            case 0 : Nt='A';
            break;
            case 1 : Nt='T';
            break;
            case 2 : Nt='G';
            break;
            case 3 : Nt='C';}
        seq[k] = Nt;}}

void AfficheSeq(char seq[], int lg){
    printf("Séquence : %c",seq[0]);
    int i;
    for(i=1;i<lg;i++){
        printf("%c",seq[i]);}
    printf("%c\n",seq[lg-1]);}

float All_GC(char seq[], float *GC1, float*GC2, float*GC3, int lg){
    float somme=0;
    float somme1=0;
    float somme2=0;
    float somme3=0;
    int p_codon;
    int k;
    for(k=1;k<lg;k+=1){
        if (seq[k] == 'G' || seq[k] == 'C'){
            somme++;
            p_codon=k%3;
            switch(p_codon){
                case 1 : somme1++;
                break;
                case 2 : somme2++;
                break;
                case 0 : somme3++;}}}
    *GC1=somme1/lg;
    *GC2=somme2/lg;
    *GC3=somme3/lg;
    return somme/lg;}

int estStart(char *seq){
    if(seq[0]=='A' && seq[1]=='T' && seq[2]=='G'){
        return 1;}
    return 0;}

int estStop(char *seq){
    if((seq[0]=='T' && seq[1]=='A' && seq[2]=='A') || (seq[0]=='T' && seq[1]=='G' && seq[2]=='A') || (seq[0]=='T' && seq[1]=='A' && seq[2]=='G')){
        return 1;}
    return 0;}

char Nt_Complementaire(char nt){
    char nt_comp;
    switch(nt){
        case 'A' : nt_comp = 'T';
        break;
        case 'T' : nt_comp = 'A';
        break;
        case 'C' : nt_comp = 'G';
        break;
        case 'G' : nt_comp = 'C';}
    return nt_comp;}

char *BrinComplementaire(char seq[], int lg){
    char *seq_comp=NewSeq(10);
    int k;
    for(k=0;k<lg;k++){
        seq_comp[k]=Nt_Complementaire(seq[k]);}
    return seq_comp;}

//float calcChi2Conformite(char *seq, int lg, float GCGlobal, float GC1, float GC2, float GC3){}

//int main(){
//    srand(time(NULL));
//    char *seq=NewSeq(8);
//    seq=ReallocSeq(seq,10);     //permet de réallouer la mémoire et donc de pouvoir modifier taille de la sqce
//    InitSeqAlea(seq,10);
//    AfficheSeq(seq,10);
//    float GC1=0.0;
//    float GC2=0.0;
//    float GC3=0.0;
//    printf("%f\n",All_GC(seq,&GC1,&GC2,&GC3,10));
//    printf("Nombre de codons start : %d\n",estStart(seq));
//    printf("Nombre de codons stop : %d\n",estStop(seq));
//    printf("Nucléotide : %c   Nucléotide complémentaire : %c\n",*seq,Nt_Complementaire(*seq));
//    char *seq_comp=BrinComplementaire(seq,10);
//    AfficheSeq(seq_comp,10);
//    FreeSeq(seq);
//    return 0;}

//dans deux cas on met un * : -quand on veut définir un tableau
//                            -quand on veut modifier une variable (sans la renvoyer)