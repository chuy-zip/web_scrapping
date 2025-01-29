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
def procesar_buffer(lexema, buffer):
    avance: int = 0
    for i in range(len(buffer)):
        avance += 1
        if buffer[i] == "eof":
            print("Lexema procesado2: " + lexema)
            return "eof", avance
        elif buffer[i] == " ":
            print("Lexema procesado: " + lexema)
            lexema = ""
        else:
            lexema += buffer[i]

    return lexema, avance




# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Buscar productos y URLs de imágenes
def extraer_productos(html):
   # Processing data using Regular Expressions.
   re_imagenes = r'<img class="img-fluid card-img-top image img-responsive" alt="item" src="(.*?)">'
   re_titulos = r'title="(.*?)"'
   re_precios = r'<h4 class="price float-end card-title pull-right">(\$\d+(?:\.\d+)?)<\/h4>'
   
   img = re.findall(re_imagenes, html) 
   titulo = re.findall(re_titulos, html) 
   precio = re.findall(re_precios, html)
   print(img)
   print(titulo)
   print(precio)

   return img, titulo, precio

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

while lexema != "eof":
   buffer = cargar_buffer(entrada, inicio, tamano_buffer)
   print(buffer)
   lexema, avance = procesar_buffer(lexema, buffer)

   inicio += avance