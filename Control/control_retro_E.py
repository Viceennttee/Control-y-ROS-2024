#control por retroaliametnación de estados
#del péndulo invertido

#importación de libreríaas
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#######################################

#parámetros del sistema

l=1 #longitud del péndulo (m)
m=1 #masa del péndulo (kg)
g=9.81 #gravedad
B=0.01 #fricción viscosa


#vector de simulación

start=0
stop=5
step=1e-3
t=np.arange(start,stop,step)
################################



#ganancias del Control

k1=5
k2=5
##############################

#ecuaciones diferenciales del sistema
def f(x,t):
    dx_dt = [0,0]
    #ley de control 

    """
    w=-k1*x[0]-k2*x[1]
    u=(m*l**2)*(((3*g)/2*l)*np.sin(x[0])+w)
    dx_dt[0]=x[1] #la derivada con respecto al tiempo en x_1 es igual a x_2
    dx_dt[1]=((3*g)/2*l)*np.sin(x[0])+(1/(m*l**2))*u
    """
    w = -k1*x[0]-k2*x[1]

    u = (m*l*2)*(3*g/2*l)*np.sin(x[0]+w)

    dx_dt[0]=x[1]

    dx_dt[1] = -(3*g/2*l)+np.sin(x[0])+(1/m*l*2)*u


    return dx_dt
#########################################



#solución de las ecuaciones diferencialees
solucion = odeint(f,y0=[math.pi/6,0],t=t)
print('Estados del péndulo ',solucion)



#gráficos de los estados
#äNGULO de los estados

plt.plot(t,solucion[:,0],'b',label='x1')
plt.xlabel('t')
plt.ylabel('x1')
plt.title('Ángulo del péndulo con respeccto al tiempo9')
plt.grid()
plt.show()



#Velocidad angular del péndulo

plt.plot(t,solucion[:,1],'r',label='x2')
plt.xlabel('t')
plt.ylabel('x2')
plt.title('Ángulo del péndulo con respeccto al tiempo9')
plt.grid()
plt.show()