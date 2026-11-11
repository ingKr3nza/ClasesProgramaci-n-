
# =============================================================================
# SECCIÓN 3: SIMULACIÓN DEL FLUJO DE TRABAJO CON GIT Y GITHUB
# =============================================================================
print("=== SECCIÓN 3: Comandos Básicos de Git y Control de Versiones ===")

git_workflow = [
    ("1. git init", "Inicializa un repositorio Git local en la carpeta del proyecto."),
    ("2. git config --global user.name 'Tu Nombre'", "Configura la identidad del desarrollador."),
    ("3. git status", "Muestra el estado de los archivos (modificados, en área de ensayo o sin rastrear)."),
    ("4. git add .", "Añade todos los archivos modificados al área de ensayo (Staging Area)."),
    ("5. git commit -m 'Clase 3: Condicionales en Python'", "Guarda una foto (snapshot) del proyecto con un mensaje descriptivo."),
    ("6. git branch -M main", "Asegura la rama principal llamada 'main'."),
    ("7. git remote add origin <URL>", "Conecta el repositorio local con el repositorio en GitHub."),
    ("8. git push -u origin main", "Sube los cambios locales al repositorio remoto en GitHub.")
]

for comando, descripcion in git_workflow:
    print(f"-> {comando.ljust(45)}: {descripcion}")

print("\n===============================================================================")
print("¡Felicidades! Has completado la práctica guiada de la Clase 3.")
print("===============================================================================")