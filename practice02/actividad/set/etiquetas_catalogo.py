def main():
    tags_laptop = {"tecnologia", "computacion", "portable"}
    tags_tablet = {"tecnologia", "pantalla_tactil", "portable"}

    print(f"Etiquetas Laptop: {tags_laptop}")
    print(f"Etiquetas Tablet: {tags_tablet}")

    # Etiquetas en común
    comunes = tags_laptop & tags_tablet
    print(f"\nEtiquetas en comun: {comunes}")

    # Etiquetas que tiene la laptop pero no la tablet
    exclusivas_laptop = tags_laptop - tags_tablet
    print(f"\nExclusivas de Laptop: {exclusivas_laptop}")

    # Todas las etiquetas unicas combinadas
    todas = tags_laptop | tags_tablet
    print(f"\nTodas las etiquetas unicas del catalogo: {todas}")


main()

# operaciones de conjunts Interseccion, Diferencia, Union
# ideal para comparar caracteristicas, etiquetas
# un producto no puede tener la misam etiqueta repetida
