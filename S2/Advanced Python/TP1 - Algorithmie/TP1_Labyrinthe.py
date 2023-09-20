import matplotlib.pyplot as plt
import random as rd

#1) Créer une liste de liste avc des nums partout et nums de pièces




N = 333

L=[]
compteur = 0
for i in range(N):
	L.append([])
	for j in range(N):
		if i==0 or i==N-1:
			L[i].append(0)
		else : 
			if j==0 or j==N-1:
				L[i].append(0)
			elif i%2!=0 and j%2!=0:
				compteur+=1
				L[i].append(compteur)
			else :
				L[i].append(0)

print(L,'\n')

wall = []
for i in range(1,N-1):
	for j in range(1,N-1):
		if i%2==1 and j%2==0 and L[i][j+1]!=L[i][j-1]:
			wall.append([i,j])
		if i%2==0 and j%2==1 and L[i-1][j]!=L[i+1][j]:
			wall.append([i,j])

n = len(wall)

while wall:
	de = rd.randint(0,len(wall)-1)
	i, j = wall[de]
	if i%2==1 and j%2==0:		
		L[i][j] = min(L[i][j-1],L[i][j+1])
		valeur = max(L[i][j-1],L[i][j+1])
		for x in range(N):
			for y in range(N):
				if valeur==L[x][y]:
					L[x][y]=L[i][j]
	if i%2==0 and j%2==1:
		L[i][j] = min(L[i-1][j],L[i+1][j])
		valeur = max(L[i-1][j],L[i+1][j])
		for a in range(N):
			for b in range(N):
				if valeur==L[a][b]:
					L[a][b]=L[i][j]
	wall = []
	for q in range(1,N-1):
		for r in range(1,N-1):
			if q%2==1 and r%2==0 and L[q][r+1]!=L[q][r-1]:
				wall.append([q,r])
			if q%2==0 and r%2==1 and L[q-1][r]!=L[q+1][r]:
				wall.append([q,r])

print(L)
plt.imshow(L, cmap=plt.get_cmap('gray'), interpolation ='None')
plt.show()

