# Ejemplo C: TypeError (Operación incompatible entre tipos)
try:
    suma_invalida = "Edad: " + 25
    print(f"Concateno: {suma_invalida}")
except TypeError as e:
    print(f"[CAPTURADO] Error de tipo: No se puede concatenar str e int directamente. ({e})")
