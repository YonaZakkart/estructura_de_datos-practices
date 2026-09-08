from collections import deque

print("Sistema de cakja y despacho\n")
# FIFo
print("1. Fila en caja")

# Crea la fila vacia
fila_caja = deque()

# Llegada de clientes
fila_caja.append("Erick")
fila_caja.append("Juan")
fila_caja.append("Yona")

print(f"Clientes en fila: {list(fila_caja)}")

# Atender clientes en orden de llegada
if len(fila_caja) > 0:
    cliente = fila_caja.popleft()
    print(f"Atendiendo a: {cliente}")

if len(fila_caja) > 0:
    cliente = fila_caja.popleft()
    print(f"Atendiendo a: {cliente}")

if len(fila_caja) > 0:
    cliente = fila_caja.popleft()
    print(f"Atendiendo a: {cliente}")

print(f"Fila después de atender: {list(fila_caja)}")

# Intentar cobrar cuando no hay clientes
if len(fila_caja) > 0:
    cliente = fila_caja.popleft()
    print(f"Atendiendo a: {cliente}")
else:
    print("Error: No se puede cobrar porque no hay nadie en la fila")


# Bolsa de productos Lifo
print("\n2. Bolsa de productos")

# Crear la bolsa como una pila
bolsa_cliente = []

# El cliente guarda productos
bolsa_cliente.append("Leche")
bolsa_cliente.append("Pan")
bolsa_cliente.append("cafe")

print(f"Productos guardados: {bolsa_cliente}")

# El cajero registra primero el ultimo producto guardado
while len(bolsa_cliente) > 0:
    producto = bolsa_cliente.pop()
    print(f"Cajero registra: {producto}")

# Intentar registrar otro producto cuando la bolsa está vacía
if len(bolsa_cliente) > 0:
    producto = bolsa_cliente.pop()
    noHagoNada = "*No hace nada*"
    print(f"Cajero registra: {producto}")
else:
    print("Error: No se puede registrars, la bolsa está vacia")


# sets
print("\n3. Membresias y cupones")

# Membresías válidas
membresias_vigentes = {
    "VIP123",
    "VIP987",
    "PREMIUM1"
}

cupones_usados = set()

# Validar una membresia
codigo_cliente = "VIP123"

if codigo_cliente in membresias_vigentes:
    print(f"Membresia {codigo_cliente} valida. Aplicando descuento")
else:
    print(f"Membresia {codigo_cliente} no es valida")


# Registrar un cupon por primera vez
cupon_ingresado = "DESC20"

if cupon_ingresado in cupones_usados:
    print(
        f"Error: El cupon {cupon_ingresado} ya fue utilizado en esta seson")
else:
    cupones_usados.add(cupon_ingresado)
    print(f"Cupon {cupon_ingresado} aplicado con exito")


# Intentar utilizar nuevamente el mismo cupón
cupon_repetido = "DESC20"

if cupon_repetido in cupones_usados:
    print(f"Error: El cupon {cupon_ingresado} ya fue utilizado en esta sesion")
else:
    cupones_usados.add(cupon_repetido)
    print(f"Cupon {cupon_ingresado} aplicado con exito")




print("\n RESUMEN")
print(f"Fila de caja al finalizar: {list(fila_caja)}")
print(f"Bolsa del cliente al finalizar: {bolsa_cliente}")
print(f"Membresias vigentes: {membresias_vigentes}")
print(f"Cupones usados: {cupones_usados}")