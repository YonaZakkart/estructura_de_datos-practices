def main():
    historial = []

    # Visitar paginas hace push a la lista
    historial.append("https://github.com/YonaZakkart")
    historial.append("https://github.com/YonaZakkart/ahorcado-python")
    historial.append("https://yonazakkart.github.io/yoro/")
    print(f"\nHistorial actual: {historial}")

    # Presionar el boton de Atras en el navegador 
    pagina_actual = historial.pop()
    print(f"\nSaliendo de: {pagina_actual}")
    print(f"Pagina activa actual: {historial[-1]}")

    # Volver a retroceder
    pagina_actual = historial.pop()
    print(f"\nSaliendo de: {pagina_actual}")
    print(f"Pagina activa actual: {historial[-1]}")

    print(f"\nHistorial restante: {historial}")

main()

# Funciona como una pila
# se registran nuevas URL con .append() y se retrocede con .pop().
