#ifndef __CODONS__
#define __CODONS__


static char tCodon2AA[64]=
{
/*AA* */
'K', 'N', 'K', 'N',
/*AC* */
'T', 'T', 'T', 'T',
/*AG* */
'R', 'S', 'R', 'S',
/*AT* */
'I', 'I', 'M', 'I',
/* CA* */
'Q', 'H', 'Q', 'H',
/* CC* */
'P', 'P', 'P', 'P',
/*CG* */
'R', 'R', 'R', 'R',
/*CT* */
'L', 'L', 'L', 'L',
/* GA* */
'E', 'D', 'E', 'D',
/* GC* */
'A', 'A', 'A', 'A',
/*GG* */
'G', 'G', 'G', 'G',
/* GT* */
'V', 'V', 'V', 'V',
/* TA* */
'*', 'Y', '*', 'Y',
/* TC* */
'S', 'S', 'S', 'S',
/* TG* */
'*', 'C', 'W', 'C',
/* TT* */
'L', 'F', 'L', 'F',
};

/*codon AAA indice 0
codon AAC indice 1
codon AAG indice 2
codon AAT indice 3
codon ACA indice 4
codon ACC indice 5
codon ACG indice 6
codon ACT indice 7
codon AGA indice 8
codon AGC indice 9
codon AGG indice 10
codon AGT indice 11
codon ATA indice 12
codon ATC indice 13
codon ATG indice 14
codon ATT indice 15
codon CAA indice 16
codon CAC indice 17
codon CAG indice 18
codon CAT indice 19
codon CCA indice 20
codon CCC indice 21
codon CCG indice 22
codon CCT indice 23
codon CGA indice 24
codon CGC indice 25
codon CGG indice 26
codon CGT indice 27
codon CTA indice 28
codon CTC indice 29
codon CTG indice 30
codon CTT indice 31
codon GAA indice 32
codon GAC indice 33
codon GAG indice 34
codon GAT indice 35
codon GCA indice 36
codon GCC indice 37
codon GCG indice 38
codon GCT indice 39
codon GGA indice 40
codon GGC indice 41
codon GGG indice 42
codon GGT indice 43
codon GTA indice 44
codon GTC indice 45
codon GTG indice 46
codon GTT indice 47
codon TAA indice 48
codon TAC indice 49
codon TAG indice 50
codon TAT indice 51
codon TCA indice 52
codon TCC indice 53
codon TCG indice 54
codon TCT indice 55
codon TGA indice 56
codon TGC indice 57
codon TGG indice 58
codon TGT indice 59
codon TTA indice 60
codon TTC indice 61
codon TTG indice 62
codon TTT indice 63
*/

#define NT2IND(n) ((n)=='A'?0:(n)=='C'?1:(n)=='G'?2:3)
/*L'inverse*/
#define IND2NT(n) ((n)==0?'A':(n)==1?'C':(n)==2?'G':'T')


/* * est un codon stop, je lui donne l'indice 20 (considere donc comme le 21e aa)*/
#define AA2IND(a) ((a)=='*'?20:(a)-'A')

#define IND2AA(i) ((i)==20?'*':(i)+'A')

/*nb aa: toutes les lettres de l'alphabet + le stop*/
#define NBAA 27


/* Indice des codons dans un tableau à une dimension*/
/* TTT -> 111 en base 4 -> 21 en base 10*/
/* On commence à partir de la gauche pour etre dans le meme ordre que le tableau du code genetique*/
#define COD2IND(c) (NT2IND((c)[0])*4*4+NT2IND((c)[1])*4+NT2IND((c)[2]))




#endif







