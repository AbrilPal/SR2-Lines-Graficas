# Andrea Abril Palencia Gutierrez, 18198
# SR2: Lines --- Graficas por computadora, seccion 20
# 20/07/2020

# importar mis funciones de points.py
from Lines import Render, color, convertir

# ancho y alto de la imagen
ancho = int(input("Ingrese el ancho deseado de la imagen: "))
alto = int(input("Ingrese el alto deseado de la imagen: "))
# ancho y alto de ViewPort
print("****************** ViewPort ******************")
ancho_v = int(input("Ingrese el ancho del ViewPort: "))
alto_v = int(input("Ingrese el alto del ViewPort: "))
# posicion del ViewPort
x_v = int(input("Ingrese la posicion en 'x' del ViewPort: "))
y_v = int(input("Ingrese la posicion en 'y' del ViewPort: "))

# color de fondo
print("****************** Color de fondo ******************")
print("Los parámetros deben ser números en el rango de 0 a 1.")
rojo = float(input("Rojo: "))
verde = float(input("Verde: "))
azul = float(input("Azul: "))

# convertir color de fondo
rojo_f = convertir(rojo)
verde_f = convertir(verde)
azul_f = convertir(azul)

# color del punto
print("****************** Color de la linea ******************")
print("Los parámetros deben ser números en el rango de 0 a 1.")
rojo = float(input("Rojo: "))
verde = float(input("Verde: "))
azul = float(input("Azul: "))

# convertir color del punto
rojo_p = convertir(rojo)
verde_p = convertir(verde)
azul_p = convertir(azul)

# crear la imagen
imagen = Render(ancho, alto, color(rojo_f,verde_f,azul_f))
imagen.glViewPort(x_v, y_v, ancho_v, alto_v)
imagen.glColor(color(rojo_p,verde_p,azul_p))
imagen.glLine(-1,-1,1,1)
imagen.glLine(-1,0, 0, 1)
imagen.glLine(0,1, 1,0)
imagen.glLine( -1, 0, 1, 0)
imagen.glFinish('Lineas.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'Lineas.bmp'.")