# Importamos los módulos necesarios
import numpy
import matplotlib.pyplot as plt
# Creamos el array x de cero a diez con cien puntos
x=numpy.linspace(0,20,100)
# Caculamos el seno de x (para los diferentes valores del array)
y=numpy.sin(x)
# Creamos una figura
plt.figure()
# Representamos
plt.plot(x,y)
# Mostramos en pantalla
plt.show()