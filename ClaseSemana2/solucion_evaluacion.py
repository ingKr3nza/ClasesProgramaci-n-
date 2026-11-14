def evaluar_estudiante(nombre: str, promedio: float, asistencia: int) -> str:
    """Evalúa la situación académica de un estudiante según promedio y asistencia."""
    if promedio >= 16.0 and asistencia >= 85:
        return "APROBADO CON MÉRITO"
    elif promedio >= 10.0 and asistencia >= 75:
        return "APROBADO"
    elif (8.0 <= promedio < 10.0) or (60 <= asistencia < 75):
        return "RECUPERACIÓN"
    else:
        return "REPROBADO"


# Programa Principal de Prueba
estudiantes = [
    {"nombre": "Carlos Mendoza", "promedio": 17.5, "asistencia": 90},
    {"nombre": "María Rodríguez", "promedio": 11.0, "asistencia": 80},
    {"nombre": "Luis Gómez", "promedio": 9.0, "asistencia": 70},
    {"nombre": "Ana Martínez", "promedio": 7.0, "asistencia": 50}
]


aprobados = 0
recuperacion = 0
reprobados = 0


for est in estudiantes:
    resultado = evaluar_estudiante(est["nombre"], est["promedio"], est["asistencia"])
    print(f"Estudiante: {est['nombre']:<18} | Estado: {resultado}")
    
    if "APROBADO" in resultado:
        aprobados += 1
    elif resultado == "RECUPERACIÓN":
        recuperacion += 1
    else:
        reprobados += 1


print(f"\nResumen: {aprobados} Aprobados | {recuperacion} En Recuperación | {reprobados} Reprobados")
