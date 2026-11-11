# ==============================================================================
# CLASE 2: EL ECOSISTEMA DE PROGRAMACIÓN Y EL MODELO MENTAL DE LAS VARIABLES (PYTHON)
# Archivo de Ejercicios Prácticos y Pruebas de Escritorio
# ==============================================================================

"""
Este archivo contiene la guía de ejercicios prácticos para la Clase 2.
Los estudiantes trabajarán individualmente y en parejas ejecutando
y completando cada sección.
"""

# ------------------------------------------------------------------------------
# SECCIÓN 1: DECLARACIÓN DE VARIABLES Y TIPOS DE DATOS PRIMITIVOS
# ------------------------------------------------------------------------------
# Instrucción: Identifica el tipo de dato de cada variable e imprime su valor y tipo en consola.

# 1.1 Enteros (int): Números sin decimales
edad_estudiante = 25
cantidad_clases = 60

# 1.2 Flotantes (float): Números con punto decimal
promedio_notas = 4.8
precio_curso = 99.99
estatura = 166.50

# 1.3 Cadenas de texto (str): Texto delimitado por comillas
nombre_profesor = "Karen"
materia = "Fundamentos de Programación"
universidad = "Escuela de Líderes Steve Jobs"

# 1.4 Booleanos (bool): Valores lógicos de verdad (True / False)
clase_activa = True
esta_lloviendo = False
debugger_activo = True

print("--- SECCIÓN 1: Tipos de Datos ---")
print("Nombre:", nombre_profesor, "| Tipo:", type(nombre_profesor))
print("Edad:", edad_estudiante, "| Tipo:", type(edad_estudiante))
print("Promedio:", promedio_notas, "| Tipo:", type(promedio_notas))
print("Estatura de la profe:", estatura, "| Tipo:", type(estatura))
print("¿Clase Activa?:", clase_activa, "| Tipo:", type(clase_activa))
print("\n")


# ------------------------------------------------------------------------------
# SECCIÓN 2: RETO DE PRUEBA DE ESCRITORIO (SEGUIMIENTO DE MEMORIA)
# ------------------------------------------------------------------------------
# Instrucción para el estudiante: ANTES de ejecutar esta sección, dibuja las "cajas de memoria"
# en tu cuaderno y predice cuál será el valor final de 'a', 'b' y 'c'.

a = 10
b = 5
c = a + b  # c vale 15

a = a + 2  # a cambia a 12
b = c - a  # b cambia a (15 - 12) = 3
c = a * b  # c cambia a (12 * 3) = 36

print("--- SECCIÓN 2: Resultado de la Prueba de Escritorio ---")
print("Valor final de a (Esperado: 12) -> Real:", a)
print("Valor final de b (Esperado: 3)  -> Real:", b)
print("Valor final de c (Esperado: 36) -> Real:", c)
print("\n")


# ------------------------------------------------------------------------------
# SECCIÓN 3: CORRECCIÓN DE BUGS Y BUENAS PRÁCTICAS (SNAKE_CASE)
# ------------------------------------------------------------------------------
# El siguiente bloque contiene errores de sintaxis y malas prácticas.
# Corrige los nombres de las variables usando la convención snake_case.

# Código con errores (Comentado):
# 1edad = 25              <- Error: No puede iniciar con número
# nombre usuario = "Ana"   <- Error: No puede tener espacios
# class = "Programación"  <- Error: 'class' es una palabra reservada

# Código Corregido:
edad_estudiante_1 = 25
apellido_usuario = "Ramirez"
nombre_clase = "Programación"

print("--- SECCIÓN 3: Buenas Prácticas de Nomenclatura ---")
print(f"Usuario: {apellido_usuario}, Edad: {edad_estudiante_1}, Clase: {nombre_clase}")
print("\n")


# ------------------------------------------------------------------------------
# SECCIÓN 4: EJERCICIO PRÁCTICO EN PAREJAS - "INTERCAMBIO DE MEMORIA"
# ------------------------------------------------------------------------------
# Problema: Tienes dos variables con valores intercambiados.
# x = "Agua"
# y = "Jugo"
# Debes lograr que 'x' contenga "Jugo" y 'y' contenga "Agua" usando una variable auxiliar.

x = "Agua"
y = "Jugo"

print("--- SECCIÓN 4: Intercambio de Variables ---")
print(f"Antes del intercambio -> x: {x}, y: {y}")

# Proceso de intercambio con variable auxiliar (vaso vacío)
vaso_auxiliar = x  # Guarda "Agua"
x = y              # 'x' ahora es "Jugo"
y = vaso_auxiliar  # 'y' ahora recibe "Agua"

print(f"Después del intercambio -> x: {x}, y: {y}")
print("\n")

# Fin del archivo de ejercicios prácticos.
