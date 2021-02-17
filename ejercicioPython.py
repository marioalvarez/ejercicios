# recorrer listas
print("1. puedes detener la aplicación escribiendo: parar")
nuevo_anillo = ""
anillos = []
while nuevo_anillo != "parar":
    nuevo_anillo = input("introduce un nuevo anillo: ")

    if nuevo_anillo != "parar":
        anillos.append(nuevo_anillo)

print("\n*********Listado de anillos*********")
for anillo in anillos:
    print(f" {anillos.index(anillo)+1}. {anillo}")
