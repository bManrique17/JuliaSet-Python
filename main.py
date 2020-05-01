import numpy
#from numba import autojit
import matplotlib.pyplot as plt
import math
import random
from PIL import Image
#@autojit

def e_complejo(z):
    ex = math.exp(z.real)
    return complex(ex*math.cos(z.imag),ex*math.sin(z.imag))

def sinh(z):
    return (e_complejo(z)-(1/e_complejo(z)))/2

def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    
    return max_iter

#Z = SinH(Z) + 1/C
#Zo = (0.90, -0.05i)

def mandelbrot2(Re, Im, max_iter):
    c = complex(Re, Im)
    z = complex(1,0.1)    
    for i in range(max_iter):   
        if z.real > 700:
            return i  
        z = sinh(z) + 1/(c*c)
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    
    return max_iter

def julia(Re, Im, max_iter, c):    
    z = complex(Re, Im)
    
    for i in range(max_iter):
        if exponent == 2:
            z = z*z + c
        elif exponent == 3:
            z = z*z*z + c
        elif exponent == 4:
            z = z*z*z*z + c
        elif exponent == 5:
            z = z*z*z*z*z + c        
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    
    return max_iter


def menu():
    print()
    print("-------MENU-------")
    print("1. Ingresar complejo")
    print("2. Generar complejo")
    print("3. Mostrar sin calidad")
    print("4. Mostrar con calidad")
    print("5. Guardar")
    print("6. Cambiar cmap")
    print("7. Cambiar enfoque")
    print("8. Cambiar exponente (2 predeterminado)")
    print("9. Random map!")
    print("0. Salir")
    return input("-> Ingrese: ")

real = -0.735
imagi = -0.2321
c = complex(real,imagi)

exponent = 2

x1 =-1
x2 = 1
y1 =-1  
y2 = 1

columns = 200
rows = 200                        
max_iter = 100
_cmap = "hot"
result = numpy.zeros([rows, columns])

while True:    
    ans = int(menu())
    if ans == 1:
        real = float(input("Parte real: "))
        imagi = float(input("Parte imaginaria: "))
        c = complex(real,imagi)
        print("**Ingresado numero "+str(c))
        nombre = str(c)+" cmap: "+str(_cmap)+" exp: "+str(exponent)+".jpg"
    elif ans == 2:
        real=random.uniform(-1, 1)
        imagi=random.uniform(-1, 1)
        c = complex(real,imagi)
        print("**Generado numero "+str(c))        
        nombre = str(c)+" cmap: "+str(_cmap)+" exp: "+str(exponent)+".jpg"
    elif ans == 3:
        columns = 200
        rows = 200          
        result = numpy.zeros([rows, columns])
        for row_index, Re in enumerate(numpy.linspace(x1, x2, num=rows)):
            for column_index, Im in enumerate(numpy.linspace(y1, y2, num=columns)):        
                result[row_index, column_index] = julia(Re, Im, max_iter, c)
        plt.figure(dpi=500)
        plt.imshow(result.T, cmap=_cmap, interpolation='bilinear', extent=[x1, x2, y1, y2])            
        plt.show()              
    elif ans == 4:
        columns = 2000
        rows = 2000        
        result = numpy.zeros([rows, columns])
        for row_index, Re in enumerate(numpy.linspace(x1, x2, num=rows)):
            for column_index, Im in enumerate(numpy.linspace(y1, y2, num=columns)):        
                result[row_index, column_index] = julia(Re, Im, max_iter, c)
        plt.figure(dpi=500)
        plt.imshow(result.T, cmap=_cmap, interpolation='bilinear', extent=[x1, x2, y1, y2])            
        plt.show()        
    elif ans == 5:     
        nombre_aux = "ERASE"+str(c)+".jpg"   
        plt.figure(dpi=500)
        plt.imshow(result.T, cmap=_cmap, interpolation='bilinear', extent=[x1, x2, y1, y2])
        plt.savefig(nombre_aux)
        im = Image.open(nombre_aux)
        width, height = im.size 
        left = 716
        top = 288
        right = 2564
        bottom = 2136
        im1 = im.crop((left, top, right, bottom)) 
        im1.save("IMG:"+nombre)

        print("**Saved!")
    elif ans == 6:                
        _cmap = input("->Ingrese nuevo cmap: ")
        print("***Changed!")
    elif ans == 7:          
        x1 = float(input("->Ingrese nuevo x1: "))
        x2 = float(input("->Ingrese nuevo x2: "))
        y1 = float(input("->Ingrese nuevo y1: "))
        y2 = float(input("->Ingrese nuevo y2: "))
        print("***Changed!")
    elif ans == 8:          
        _exponent = int(input("->Ingrese nuevo exponente (entre 2 y 5): "))
        if ((exponent > 1) and (exponent < 6)):
            exponent = _exponent
            print("***Changed!")        
    elif ans == 9:          
        columns = int(input("->Ingrese columnas: "))
        rows = int(input("->Ingrese filas: "))      
        limite = int(input("->Ingrese limite del random: "))   
        name = random.randrange(9999)
        nombre = "rand:"+str(limite)+" cmap: "+str(_cmap)+str(name)+".jpg"
        result = numpy.zeros([rows, columns])
        flag = True
        for row_index, Re in enumerate(numpy.linspace(x1, x2, num=rows)):
            for column_index, Im in enumerate(numpy.linspace(y1, y2, num=columns)):     
                if flag:   
                    result[row_index, column_index] = limite*4
                    flag = False
                else:
                    result[row_index, column_index] = random.randrange(limite)
        plt.figure(dpi=500)
        plt.imshow(result.T, cmap=_cmap, interpolation='bilinear', extent=[x1, x2, y1, y2])            
        plt.show()  
    elif ans == 0:                
        print("***Bai***")
        break

'''
    
   '''     