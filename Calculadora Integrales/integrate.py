import sympy
from scipy.integrate import quad


def calcular_error(funcion, limites):
    resultado, error = quad(funcion, limites[0], limites[1])
    return resultado, error

print("Funcion polinómica F(x)= a*x^n: ")
def funcionN1(a, n, limite_inferior, limite_superior):
    x = sympy.symbols("x")
    f = a * x**n

    print("Funcion a integrar acomodada", f)

    integral = (x**(n + 1) / (n + 1))
    print("Integral resuelta: ", integral)

    area = (limite_superior**(n + 1) / (n + 1)) - (limite_inferior**(n + 1) / (n + 1))
    print("Area de integral resuelta: ", area)

    # Calcular la integral y el error usando scipy
    funcion_scipy = sympy.lambdify(x, f, 'numpy')
    resultado_scipy, error_scipy = calcular_error(funcion_scipy, [limite_inferior, limite_superior])

    print(f"El error cometido en la integración es: {error_scipy:.15e}")

# Input de usuario para la primera función
a1 = sympy.symbols("a", real=True)
n = sympy.symbols("n", whole=True)

a1 = int(input("Ingrese el valor de a: "))
n = int(input("Ingrese el valor de n: "))
limite_inferior = int(input("Ingrese el límite inferior: "))
limite_superior = int(input("Ingrese el límite superior: "))

# Calcular el área para la primera función
funcionN1(a1, n, limite_inferior, limite_superior)

print("\n")

print("Funcion polinómica de segundo grado F(x)= a*x^2 + b*x + c: ")
def funcionN2(a, b, c, limite_inferior, limite_superior):
    x = sympy.symbols("x")
    f = a * x**2 + b * x + c

    print("Integral acomodada: ", f)

    integral = (a * x**3 / 3) + (b * x**2 / 2) + c * x
    print("Integral resuelta: ", integral)

    area = (limite_superior**(2 + 1) / (2 + 1)) + (limite_superior**b) + (c * limite_superior) - (limite_inferior**(2 + 1) / (2 + 1)) + (limite_inferior**b) + (c * limite_inferior)
    print("Area de integral resuelta: ", area)

    # Calcular la integral y el error usando scipy
    funcion_scipy = sympy.lambdify(x, f, 'numpy')
    resultado_scipy, error_scipy = calcular_error(funcion_scipy, [limite_inferior, limite_superior])

    print(f"\nLa integral de la función con los límites de integración es: {resultado_scipy:.15f}")
    print(f"El resultado de la integración (área obtenida) es: {resultado_scipy:.15f}")
    print(f"El error cometido en la integración es: {error_scipy:.15e}")

# Input de usuario para la segunda función
a2 = sympy.symbols("a", real=True)
b2 = sympy.symbols("b", real=True)
c2 = sympy.symbols("c", real=True)

a2 = int(input("Ingrese el valor de a: "))
b2 = int(input("Ingrese el valor de b: "))
c2 = int(input("Ingrese el valor de c: "))
limite_inferior = int(input("Ingrese el límite inferior: "))
limite_superior = int(input("Ingrese el límite superior: "))

# Calcular el área para la segunda función
funcionN2(a2, b2, c2, limite_inferior, limite_superior)

print("\n")

print("Funcion trigonometrica F(x)= A * sin(k*x): ")
def funcionN3(A, k, limite_inferior_fraccion, limite_superior_fraccion):
    x = sympy.symbols("x")
    f = A * sympy.sin(k * x)

    print("integral acomodada", f)

    integral = -A * sympy.cos(k * x) / k
    print("integral resuelta", integral)

    integral_superior = -A * sympy.cos(k * limite_superior_fraccion) / k
    integral_inferior = -A * sympy.cos(k * limite_inferior_fraccion) / k
    area = integral_superior - integral_inferior

    print("area de integral resuelta", area)

    # Calcular la integral y el error usando scipy
    funcion_scipy = sympy.lambdify(x, f, 'numpy')
    resultado_scipy, error_scipy = calcular_error(funcion_scipy, [limite_inferior_fraccion, limite_superior_fraccion])

    print(f"\nLa integral de la función con los límites de integración es: {resultado_scipy:.15f}")
    print(f"El resultado de la integración (área obtenida) es: {resultado_scipy:.15f}")
    print(f"El error cometido en la integración es: {error_scipy:.15e}")

# Input de usuario para la tercera función
A3 = sympy.symbols("A", real=True)
k3 = sympy.symbols("k", real=True)

A3 = int(input("Ingrese el valor de A: "))
k3 = int(input("Ingrese el valor de k: "))
limite_inferior3 = int(input("Ingrese el límite inferior (en grados): "))
limite_superior3 = int(input("Ingrese el límite superior (en grados): "))
pi = sympy.pi
limite_inferior_fraccion3 = limite_inferior3 * pi / 180
limite_superior_fraccion3 = limite_superior3 * pi / 180

# Calcular el área para la tercera función
funcionN3(A3, k3, limite_inferior_fraccion3, limite_superior_fraccion3)
