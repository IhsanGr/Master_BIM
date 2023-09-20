

#ifndef __MANIP_SEQ_SIMPLE__
#define __MANIP_SEQ_SIMPLE__

char *NewSeq(int lg);
char *ReallocSeq(char *seq, int lg);
void FreeSeq(char *seq);


void InitSeqAlea(char seq[], int lg);
void AfficheSeq(char seq[], int lg);
float GC(char seq[], int lg);
char Nt_Complementaire(char nt);
char *BrinComplementaire(char seq[], int lg);
int estStart(char *seq);
int estStop(char *seq);
int compteGC3en3(char *seq, int lgSeq);
float calcChi2Conformite(char *seq, int lg, float GCGlobal );


#endif
