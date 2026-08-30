def main():
    # Coordenadas latitud, longitud y Altitud
    punto_interes = (13.6929, -89.2182, 650.5)
    print(f"Registro de coordenada: {punto_interes}")

    lat, lon, alt = punto_interes
    print(f"Latitud: {lat}° | Longitud: {lon}° | Altitud: {alt}m")

    # inmutabilidad
    #descomentar la linea siguiente provocaría un TypeError :p
    # punto_interes[0] = 14.0000

main()

# la ubicacionde un punto fijo no debe alterarse
# permite extraer las componentes de forma limpia
# si un dato cambi representa un punto nuevo no una modificacion del actual
