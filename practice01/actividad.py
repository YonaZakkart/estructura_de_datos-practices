class CodigoPostal:
    def __init__(self, valor):
        # Evita aceptar codigos postales que no tengan exactamente 4 dígitos.
        if not isinstance(valor, str) or not valor.isdigit() or len(valor) != 4:
            raise ValueError("El codigo postal debe tener exactamente 4 dígitos")
        self.valor = valor

    def __str__(self):
        return self.valor


class Telefono:
    def __init__(self, valor):
        # Evita aceptar números de telefono que no tengan exactamente 8 dígitos.
        if not isinstance(valor, str) or not valor.isdigit() or len(valor) != 8:
            raise ValueError("El telfono debe tener exactamente 8 dígitos.")
        self.valor = valor

    def __str__(self):
        return self.valor


class Porcentaje:
    def __init__(self, valor):
        # Evita aceptar porcentajes menores que 0 o mayores que 100.
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        self.valor = valor

    def __str__(self):
        return str(self.valor)


class Contrasenia:
    def __init__(self, valor):
        # Evita aceptar contrasenias demasiado cortas 
        if not isinstance(valor, str) or len(valor) < 8:
            raise ValueError("La contrasenia debe tener al menos 8 caracteres")
        self.valor = valor

    def __str__(self):
        return self.valor


class Temperatura:
    def __init__(self, valor):
        # Evita aceptar temperaturas ,uy inferiores
        if not isinstance(valor, (int, float)) or valor < -270:
            raise ValueError("La temperatura no puede ser menor que -270 °C.")
        self.valor = valor

    def __str__(self):
        return str(self.valor)


# USo
try:
    # Caso valido
    codigo1 = CodigoPostal("1001")
    print("Cdigo postal valido:", codigo1)

    # Caso invalido, tiene menos de 4 
    codigo2 = CodigoPostal("123")
    print("Codigo postal válido:", codigo2)

except ValueError as e:
    print("Codigo postal invalido:", e)


try:
    # Caso valido
    telefono1 = Telefono("12345678")
    print("Telefono valido:", telefono1)

    # Caso mp valido tiene menos de 8 num
    telefono2 = Telefono("9876543")
    print("Telefono valido:", telefono2)

except ValueError as e:
    print("Telefono inválido:", e)


try:
    # Caso válido
    porcentaje1 = Porcentaje(75)
    print("Porcentaje valido:", porcentaje1)

    # Caso inválido: supera el 100%
    porcentaje2 = Porcentaje(150)
    print("Porcentaje valido:", porcentaje2)

except ValueError as e:
    print("Porcentaje no valido:", e)


try:
    # Caso valido
    contrasena1 = Contrasenia("Python123")
    print("Contraseña válida:", contrasena1)

    # Caso invalido pq tiene menos de 8 caracteres
    contrasena2 = Contrasenia("1234")
    print("Contrasenia :", contrasena2)

except ValueError as e:
    print("Contrasenia invalida:", e)


try:
    temperatura1 = Temperatura(25)
    print("Temperatura:", temperatura1)

    temperatura2 = Temperatura(-300)
    print("Temperatura:", temperatura2)

except ValueError as e:
    print("Temperatura invlida:", e)