#       GESTION DE BIBLIOTECA

#   TUPLA : ID, Titulo y Autor
# ficha inmutable de un libro.
# los datos clave del libro no cambien

#   SET :prestados_id
# Almacena los ID de los libros en prestamo
# Evita duplicar registros de préstamos
# permite verificar si un libro esta disponible o no

#   LISTA historial_prestamos
# Registra en orden todas las acciones realizadas
# Conserva la secuencia temporal de las operaciones


def main():
    # Catalogo de Libros - Tuplas inmutables
    libro1 = ("58321", "El nombre del viento", "Patrick Rothfuss")
    libro2 = ("72367", "Omniscient Readers Viewpoint", "Sing-Shong")
    libro3 = ("18237", "Lord of the Mysteries", "Cuttlefish That Loves Diving")

    # Control de estado - Set para bsqueda rapida y evitar duplicados
    prestados_id = set()

    # registro - Lista para mantener el orden cronologico
    historial_prestamos = []

    print("\nSISTEMA DE BIBLIOTECA")

    # Registrar prestamo del libro 1
    libro_id, titulo, autor = libro1
    if libro_id not in prestados_id:
        prestados_id.add(libro_id)
        historial_prestamos.append(f"PRESTAMO: '{titulo}' (ID: {libro_id})")
        print(f"\nLibro prestado: \nNombre: {titulo} \nAutor: {autor}")

    # Intentar prestar el mismo libro otra ve
    if libro_id in prestados_id:
        print(f"\nERROR: El libro '{titulo}' ya esta prestado")

    # Registrar prestamo del libro 2 y 3
    libro_id2, titulo2, autor2 = libro2
    if libro_id2 not in prestados_id:
        prestados_id.add(libro_id2)
        historial_prestamos.append(
            f"PRESTAMO: '{titulo2}' (ID: {libro_id2})")
        print(f"\nLibro prestado: \nNombre: {titulo2} \nAutor: {autor2}")

    libro_id3, titulo3, autor3 = libro3
    if libro_id3 not in prestados_id:
        prestados_id.add(libro_id3)
        historial_prestamos.append(
            f"PRESTAMO: '{titulo3}' (ID: {libro_id3})")
        print(f"\nLibro prestado: \nNombre: {titulo3} \nAutor: {autor3}")

    # Devolver el libro 1
    prestados_id.remove(libro_id)
    historial_prestamos.append(f"DEVOLUCION: '{titulo}' (ID: {libro_id})")
    print(f"\nLibro devuelto: {titulo}")

    # Resumen
    print("\nESTADO DE LA BIBLIOTECA")
    print(
        f"Libros actualmente prestados (set - IDs unicos): \n{prestados_id}")
    print("\nHistorial de Operaciones (Lista - Orden Cronologico):")
    for l_id, evento in enumerate(historial_prestamos, start=1):
        print(f"  {l_id}. {evento}")


main()
