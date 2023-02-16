mat=[]

filas=int(input("cantidad de filas: "))
columnas = int(input("cantidad de columnas: "))

for i in range(filas):
    mat.append([0]*columnas)

print(mat)


for f in range(filas):
    for c in range (columnas):
        mat[f][c]= int(input("Elemento posicion %d , %d:  "%(f,c)))

print(mat)