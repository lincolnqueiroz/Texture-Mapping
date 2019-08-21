from PIL import Image
from pylab import *
import homografia

sX = [870,1257,1717,1405]
sY = [2037,2863,2512,1889]
#Coordenadas de onde a textura deve ser alocada

def prox(A):
	#Retorna inteiro mais próximo
	if 2*A < 2*int(A) + 1:
		return int(A)
	return int(A+1)

scene = array(Image.open("scene.jpg")) #Importa cenário
texture = array(Image.open("textura.jpg")) #Importa textura
y,x = scene.shape[:2] #Dimensões do cenário (x,y)
sceneP = array([X,Y,[1,1,1,1]]) #Vetoriza os pontos onde a textura vai entrar
m,n = texture.shape[:2] #Dimensões da textura (n,m)
textureP = array([[0,0,n,n],[0,m,m,0],[1,1,1,1]]) #Vetoriza os pontos da textura
H = homografia.getH(sceneP,textureP)
H_1 = linalg.inv(H) #Calcula a inversa de H
for i in range(x):
	for j in range(y):
		aux = array([i, j, 1])
		aux = aux.transpose()
		ponto = dot(H_1,aux) #H_1 * [i j 1]^T
		ponto = ponto.transpose() #Transforma em linha
		a = prox(ponto[0]/ponto[2]) #Normaliza e aproxima para o pixel mais próximo
		b = prox(ponto[1]/ponto[2])
		if a in range(n) and b in range(m): #Verifica se cai dentro da textura
			scene[j][i] = texture[b][a] #Substituição pela textura
plot(X,Y,"r*") #Delimitação visual do espaço onde entra a textura
imshow(scene)
show()
