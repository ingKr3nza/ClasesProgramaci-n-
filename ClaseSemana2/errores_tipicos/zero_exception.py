# Un error de tiempo de ejecución (Runtime Error) ocurre cuando el código es 
# sintácticamente válido pero falla durante la ejecución al procesar datos inválidos.

# Ejemplo A: ZeroDivisionError
try:
    numerador = 100
    denominador = 0
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(f"[CAPTURADO] Error matemático: No se puede dividir entre cero. ({e})")

