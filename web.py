# Importing the required libraries.
import re
import csv
# Actividad Práctica: Implementación de un Búfer de Entrada
# Diseño de lenguajes de programación
"""
Integrantes del grupo:
Nelson García 22434
Joaquín Puente 22296
Ricardo Chuy 221007
Diego Linares 221256
"""

# Se carga el buffer
def cargar_buffer(entrada: list[str], inicio: int, tamano_buffer: int) -> (list[str]):
    buffer: list[str] = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

# Procesar y extraer lexemas del buffer
def procesar_buffer(lexema, buffer, prop_list):
    avance: int = 0
    for i in range(len(buffer)):
        avance += 1
        if buffer[i] == "eof":
            print("Lexema procesado: " + lexema)
            extraer_productos(lexema,prop_list)
            return "eof", avance
        elif buffer[i] == "\n":
            print("Lexema procesado: " + lexema)
            extraer_productos(lexema,prop_list)
            lexema = ""
        else:
            lexema += buffer[i]

    return lexema, avance

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Buscar productos y URLs de imágenes
def extraer_productos(html_line, prop_list: list[str]):
   # Processing data using Regular Expressions.
   re_imagenes = r'<img class="img-fluid card-img-top image img-responsive" alt="item" src="(.*?)">'
   re_titulos = r'title="(.*?)"'
   re_precios = r'<h4 class="price float-end card-title pull-right">(\$\d+(?:\.\d+)?)<\/h4>'
   
   #Este es el orden del html para las caracteristicas de un producto
   img:list[str] = re.findall(re_imagenes, html_line) 
   precio:list[str] = re.findall(re_precios, html_line)
   titulo:list[str] = re.findall(re_titulos, html_line) 

   print(img)
   print(titulo)
   print(precio)

   if len(img) != 0:
       prop_list.append(img[0])
   
   if len(precio) != 0:
       prop_list.append(precio[0])

   if len(titulo) != 0:
       prop_list.append(titulo[0])


# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nombre del Producto', 'URL de la Imagen'])
        writer.writerows(productos)

html = cargar_html("test.html")
#print(html)

inicio = 0
avance = 0
tamano_buffer = 10
lexema = ""

entrada = list(html)
print(len(entrada))

# lista donde se van a guardar las propiedades. Al final la lista debería tener las propiedades en el siguiente orden
# [img1,titulo1,precio1,img2,titulo2,precio2,....]
prop_list = []

while lexema != "eof":
   buffer = cargar_buffer(entrada, inicio, tamano_buffer)
   print(buffer)
   lexema, avance = procesar_buffer(lexema, buffer, prop_list)

   inicio += avance

print("\nFinal: ", prop_list)

#Ahora hace falta la parte del ouput