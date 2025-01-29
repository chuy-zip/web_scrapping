# Importing the required libraries.
import re
import csv

# Abrir archivo HTML
def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

# Buscar productos y URLs de imágenes
def extraer_productos(html):
    regex_nombre = r"<h2>(.*?)</h2>"
    regex_imagen = r"<img src='(.*?)' alt='product-image'/>"
    nombres = re.findall(regex_nombre, html)
    imagenes = re.findall(regex_imagen, html)
    return zip(nombres, imagenes)

# Exportar resultados a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nombre del Producto', 'URL de la Imagen'])
        writer.writerows(productos)


html = cargar_html("test.html")
#print(html)

# Processing data using Regular Expressions.
re_imagenes = r'<img class="img-fluid card-img-top image img-responsive" alt="item" src="(.*?)">'
re_titulos = r'title="(.*?)"'
re_precios = r'<h4 class="price float-end card-title pull-right">(\$\d+(?:\.\d+)?)<\/h4>'

print(re.findall(re_imagenes, html))
print(re.findall(re_titulos, html))
print(re.findall(re_precios, html))