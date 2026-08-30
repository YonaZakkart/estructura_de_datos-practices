def main():
    playlist = ["Three little birds", "Earned it", "Blinding Lights"]
    print(f"\nPlaylist inicial: {playlist}")

    # Agregar canciones 
    playlist.append("Strobe")
    playlist.append("Blinding Lights")  # Se puede duplicado
    print(f"\nDespuus de agregar temas: {playlist}")

    # Reproducir (eliminar la primera canción)
    reproduciendo = playlist.pop(0)
    print(f"\nreproduciendo: '{reproduciendo}'")
    print(f"Playlist restante: {playlist}")

    # Insertar una canción en la siguiente posicion
    playlist.insert(0, "Clair de Lune")
    print(f"\nPlaylist con tema prioritario: {playlist}")

main()

# 1. las canciones se reproducen en el orden en que se agregan
# 2. permie aniadir canciones al final o eliminar temas ya escuchados .
# 3. un usuario puede tener la misma canción varias veces
