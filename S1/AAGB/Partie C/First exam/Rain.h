typedef struct _tyCase {
	int barre;
	int eau;
} tyCase;


void afficheRainWatter(tyCase *tab, int n);
void fillWater( tyCase tab[], int n);
int sommeTab(tyCase tab[], int n);
tyCase *lire_tableau(char *nomFichier, int *p_nbVal);
int maximumBarreTab(tyCase tab[], int n);
int compter_lignes(char *nomFichier);
