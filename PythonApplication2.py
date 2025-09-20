# Solicitar la nota
import math


nota = int(input("Ingrese una nota (0–20): "))

# Validar rango
if nota < 0 or nota > 20:
    print("Error: nota fuera de rango.")
else:
    # Clasificación usando "simulación de switch" con if-elif
    if 0 <= nota <= 10:
        print("Desaprobado")
    elif 11 <= nota <= 13:
        print("Regular")
    elif 14 <= nota <= 17:
        print("Bueno")
    elif 18 <= nota <= 20:
        print("Excelente")

    # Condicionales adicionales
    if nota >= 14 and nota % 2 == 0:
        print("Buen desempeño con nota par")

    if nota < 11 or nota % 2 != 0:
        print("Necesita reforzar")

    # Cálculos
    raiz = math.sqrt(nota)
    cubo = nota ** 3

    print(f"Raíz cuadrada: {raiz:.1f}")
    print(f"Potencia al cubo: {cubo}") 
 
