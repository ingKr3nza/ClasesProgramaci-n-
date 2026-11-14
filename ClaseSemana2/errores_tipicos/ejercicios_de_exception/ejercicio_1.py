print("=== SECCIÓN 2: Control Completo de Flujo con try-except-else-finally ===")

def calcular_promedio_seguro(suma_notas, cantidad_estudiantes):
    """
    Calcula el promedio de notas de forma segura manejando posibles excepciones.
    """
    try:
        # Intento de cálculo
        promedio = suma_notas / cantidad_estudiantes
    except ZeroDivisionError:
        print("[ERROR] La cantidad de estudiantes no puede ser cero.")
        return None
    except TypeError:
        print("[ERROR] Los valores ingresados deben ser numéricos (int o float).")
        return None
    else:
        # Se ejecuta ÚNICAMENTE si no ocurrió ninguna excepción en el bloque try
        print(f"[ÉXITO] Cálculo realizado correctamente.")
        return promedio
    finally:
        # Se ejecuta SIEMPRE, haya ocurrido error o no (ideal para limpieza/registros)
        print("[REGISTRO] Operación de cálculo finalizada.")

# Pruebas de la función
print("\nPrueba 1 (Válida):")
res1 = calcular_promedio_seguro(85.5, 5)
print(f"Resultado: {res1}")

print("\nPrueba 2 (División por Cero):")
res2 = calcular_promedio_seguro(100, 0)
print(f"Resultado: {res2}")