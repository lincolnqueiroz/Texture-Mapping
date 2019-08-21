import numpy as np

def getH(scene,texture):
	if scene.shape != texture.shape:
		raise RuntimeError("Numero de pontos diferentes")
	coluna = []
	#Cria tabela 12x12 para resolver o sistema do caderno do Paes Leme, levando a textura no cenário
	for i in range(4):
		for j in range(3):
			linha = np.array([])
			if j % 3 == 0:
				linha = np.append(linha,[texture[0][i],texture[1][i],texture[2][i]])
				linha = np.append(linha,[0,0,0,0,0,0])
				if i == 0:
					linha = np.append(linha,[0,0,0])
				if i == 1:
					linha = np.append(linha,[-scene[j][i]])
					linha = np.append(linha,[0,0])
				if i == 2:
					linha = np.append(linha,[0])
					linha = np.append(linha,[-scene[j][i]])
					linha = np.append(linha,[0])
				if i == 3:
					linha = np.append(linha,[0,0])
					linha = np.append(linha,[-scene[j][i]])
					
			if j % 3 == 1:
				linha = np.append(linha,[0,0,0])
				linha = np.append(linha,[texture[0][i],texture[1][i],texture[2][i]])
				linha = np.append(linha,[0,0,0])
				if i == 0:
					linha = np.append(linha,[0,0,0])
				if i == 1:
					linha = np.append(linha,[-scene[j][i]])
					linha = np.append(linha,[0,0])
				if i == 2:
					linha = np.append(linha,[0])
					linha = np.append(linha,[-scene[j][i]])
					linha = np.append(linha,[0])
				if i == 3:
					linha = np.append(linha,[0,0])
					linha = np.append(linha,[-scene[j][i]])

			if j % 3 == 2:
				linha = np.append(linha,[0,0,0,0,0,0])
				linha = np.append(linha,[texture[0][i],texture[1][i],texture[2][i]])
				if i == 0:
					linha = np.append(linha,[0,0,0])
				if i == 1:
					linha = np.append(linha,[-scene[j][i]])
					linha = np.append(linha,[0,0])
				if i == 2:
					linha = np.append(linha,[0])
					linha = np.append(linha,[-scene[j][i]])
					linha = np.append(linha,[0])
				if i == 3:
					linha = np.append(linha,[0,0])
					linha = np.append(linha,[-scene[j][i]])		
			coluna.append(linha)

	A = np.asarray(coluna)
	b = np.array([scene[0][0],scene[1][0],1,0,0,0,0,0,0,0,0,0])
	R = np.linalg.solve(A,b) #Solução do sistema
	aux = []
	for i in range(3):
		aux.append([R[3*i],R[3*i+1],R[3*i+2]]) #Montagem da matriz H
	H = np.asarray(aux)
	return H
