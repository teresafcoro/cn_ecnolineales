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

# Ejercicio 3
def newton(f, df, x0, tol=1.e-6, n=100):    
    for i in range(n):
        x1 = x0 - f(x0)/df(x0)      
        if abs(x1 - x0) < tol:                   
            break
        x0 = x1    
    return x1, i+1

def raices_newton(f, df, a, b, tol = 1.e-6, maxiter = 100, n = 100):
    intervalos = busquedaIncremental(f, a, b, n)
    y = np.zeros((n, 1))
    cont = 0
    for x in intervalos:
        sol, i = newton(f, df, x[0])
        y[cont,:]  = sol
        cont += 1
    return y[:cont,:] 

f  = lambda x: x**4 + 2 * x**3 - 7 * x**2 + 3
df = lambda x : 4 * x**3 + 6 * x**2 - 14 * x
print('Raíces reales de f en [-4., 4.]\n', raices_newton(f, df, -4., 4.))