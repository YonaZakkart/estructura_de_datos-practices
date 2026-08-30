def main():
    #            (HOST, PUERTO, MODO_DEBUG, PROTOCOLO)
    config_db = ("localhost", 5432, False, "postgresql")
    print(f"Configuracion de base de datos: {config_db}")

    # Acceso a valores mediante índices
    print(f"Conectando a {config_db[3]}://{config_db[0]}:{config_db[1]}")
    if not config_db[2]:
        print("Modo DEBUG: Desactivado")
    else:
        print("Modo DEBUG: Activado")

main()


# parametro fijos que no deben cambiar durante la ejecucion
# menor consumo de memoria :b
