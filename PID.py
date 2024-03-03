#CONTROL PID
import numpy as np 
import matplotlib.pyplot as plt
import control
import math

#creamos el vector de simulación, de tiempo 
start=0
stop=10
step=1e-3
t=np.arange(start,stop,step)


##################################
numerador_gp=np.array([1])
denominador_gp=np.array([1,2])
gp=control.tf(numerador_gp,denominador_gp)
print('gp(s)=', gp)

#parámetros del control PID
kp=1
ti=2/3
td=1/2

#función de transferencia del PID
numerador_pid=np.array([kp*ti*td,kp*ti,kp])
denominador_pid=np.array([ti,0])
c=control.tf(numerador_pid,denominador_pid)
print('control PID', c)

#función de transferencia de trayectoria directa 

g=control.series(c,gp)

print('función de transferencia de trayectoria directa')
print('G(s)=', g)

#Se necesita construir el bloque h para poder restar
#Función de transferencia de retroalimentación
numerador_h=np.array([1])
denominador_h=np.array([1])
h=control.tf(numerador_h,denominador_h)

#Función de transferencia total
T=control.feedback(g,h)
print('función de transferencia total')
print('T(s)=', T)
######################################################
#Polos de la función de transferencia total
polos=control.pole(T)
print('polos de T(s)',polos )

#los ceros determinan la fase, sistema de fase mínima
#si la parte real de los ceros es positiva el sistema responde del lado contrario por un instante y luego
#ya se comporta de buena manera 

#investigar que es diagram de BODE
#investigar NIGHT
ceros=control.zero(T)
print('ceros de T(s)', ceros)

control.pzmap(T) #graficar
plt.grid()
plt.show()
#######################
#ley de control
t,y=control.step_response(T)
plt.plot(t, y)
plt.title('Control PID')
plt.xlabel('tiempo')
plt.ylabel('y(t)')
plt.grid()
plt.show()