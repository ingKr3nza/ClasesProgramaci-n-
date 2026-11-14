# Ejemplo B: ValueError (Conversión fallida de tipo)
try:
    entrada_usuario = "veinte"
    numero = int(entrada_usuario)
    print(f"Resultado del cambio: {numero}")
except ValueError as e:
    print(f"[CAPTURADO] Error de valor: Imposible convertir '{entrada_usuario}' a entero. ({e})")