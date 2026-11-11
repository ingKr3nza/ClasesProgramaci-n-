# =============================================================================
# SECCIÓN 2: ESTRUCTURAS CONDICIONALES (if, elif, else)
# =============================================================================
print("=== SECCIÓN 2: Control de Flujo con Condicionales ===")

puntuacion_proyecto = 75

if puntuacion_proyecto >= 90:
    nivel = "Excelencia Tecno-Líder (A)"
elif puntuacion_proyecto >= 80:
    nivel = "Desempeño Destacado (B)"
elif puntuacion_proyecto >= 70:
    nivel = "Aprobado Aceptable (C)"
else:
    nivel = "Requiere Re-evaluación"

print(f"Puntuación obtenida: {puntuacion_proyecto} puntos.")
print(f"Clasificación asignada: {nivel}\n")