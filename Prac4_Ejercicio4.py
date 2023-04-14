import numpy as np

# Ejercicio 1
def busquedaIncremental(f, a, b, n):
    x = np.linspace(a,b,n+1)
    intervalos = np.zeros((n,2))
    y = f(x)
    contador = 0    
    for i in range(n):
        if y[i]*y[i+1] < 0:
            intervalos[contador,:] = x[i:i+2]
            contador += 1            
    intervalos = intervalos[:contador,:]    
    return intervalos

# Ejercicio 2
def biseccion(f, a, b, tol=1.e-6, n=100):
    if f(a)*f(b) > 0.0: 
        print('La función tiene el mismo signo en los extremos')
    for i in range(n):
        m = 0.5*(a + b)                
        if f(a)*f(m) < 0: 
            b = m;
        elif f(m)*f(b) < 0:  
            a = m
        else:
            break
        if b - a < tol:
            break    
    return m,i+1 # i+1 porque el cero también cuenta

def raices_bisec(f, a, b, tol = 1.e-6, maxiter = 100, n = 100):
    intervalos = busquedaIncremental(f, a, b, n)
    y = np.zeros((n, 1))
    cont = 0
    for x in intervalos:
        sol, i = biseccion(f, x[0], x[1])
        y[cont,:]  = sol
        cont += 1
    return y[:cont,:] 

f = lambda x: np.cos(x) ** 2 + x/10
print('Raíces reales de f en [-10., 0.]\n', raices_bisec(f, -10., 0.))