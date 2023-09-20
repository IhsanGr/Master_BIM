#ifndef __MANIP_SEQ_ADN__
#define __MANIP_SEQ_ADN__

typedef struct {
	char *seq;
	int lg;
	float GC;
} tySeqADN;

tySeqADN* newSeqADN();
void freeSeqADN(tySeqADN *pS);
tySeqADN* complementaire(tySeqADN *pS);
int CompterNbSeq(char *nomFi);
tySeqADN *LireUneSeqFasta(FILE *pFi);
tySeqADN *LireFastaSimple(char *nomFi);
tySeqADN **LireFastaMul(char *nomFi, int *nbSeq);

#endif