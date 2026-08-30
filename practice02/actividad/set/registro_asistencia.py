def main():
    asistentes = set()

    # registro
    # con duplicados por error del usuario
    registros_entrantes = [
        "yona@gmail.com",
        "maria@gmail.com",
        "yona@gmail.com",  # Duplicado
        "carlos@gmail.com",
        "carlos@gmail.com" # Duplicado
    ]

    for correo in registros_entrantes:
        asistentes.add(correo)

    print(f"\nTotal de registros : {len(registros_entrantes)}")
    print(f"\nAsistentes unicos registrados ({len(asistentes)}): {asistentes}")

    # Verificacion de presencia
    consulta = "yona@gmail.com"
    if consulta in asistentes:
        print(f"\nEl correo '{consulta}' ya ingresó al evento")

main()

# si un participante intenta registrarse varias veces, solo se guarda una vez.
# No requiere un orden solo interesa la presencia unica del elemento.
