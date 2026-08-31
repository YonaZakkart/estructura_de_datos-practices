# Permisos que necesita el sistema
permisos_necesarios = {"leer", "escribir", "borrar"}

# Permisos que tiene el usuario
permisos_usuario = {"leer", "escribir"}

# Comprobamos si tiene todos permisos
if permisos_necesarios.issubset(permisos_usuario):
    print("El usuario tiene todos los permisos")
else:
    print("El usuario no tiene todos los permisos")

# Mostramos los permisos que le faltan
faltantes = permisos_necesarios - permisos_usuario

print("Permisos faltantes:", faltantes)
