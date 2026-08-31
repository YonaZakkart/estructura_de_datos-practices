from collections import deque

#una cola para los clientes
cola = deque()

# Agregamos clientes
cola.append("Requeno")
cola.append("Carlos")
cola.append("Pocho")

print("Clientes en espera:", list(cola))

# Atendemos al primer cliente que llego
cliente = cola.popleft()

print("Cliente atendido:", cliente)
print("Clientes restantes:", list(cola))
