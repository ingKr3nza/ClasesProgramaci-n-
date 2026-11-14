print("=== SECCIÓN 3: Patron de Entrada Defensiva con Bucles ===")

def solicitar_edad_valida():
    """
    Solicita repetidamente al usuario su edad hasta que ingrese un entero positivo válido.
    """
    while True:
        try:
            # Simulación de lectura de datos de entrada
            entrada = input("Ingrese su edad (número entero positivo): ")
            edad = int(entrada)
            if edad < 0 or edad > 120:
                print("[VALIDACIÓN] La edad debe estar entre 0 y 120 años. Intente de nuevo.")
                continue
            return edad
        except ValueError:
            print("[ERROR] Entrada no válida. Por favor, ingrese un número entero (ej. 18).")

# Descomentar para probar de forma interactiva en la terminal:
edad_confirmada = solicitar_edad_valida()
print(f"Edad validada con éxito: {edad_confirmada}")