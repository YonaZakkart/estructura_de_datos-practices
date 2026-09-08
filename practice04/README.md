## Practica 4: Integración de FIFO, LIFO y Sets en Python

Esta carpeta contiene una serie de ejercicios de la practica 4. 
Trabajaremos la interacción simultánea de colas de atención al cliente (FIFO), pilas de inventario/canastas (LIFO) y validación de promociones únicas con conjuntos (Sets).

### Estructura del Proyecto

```text
.
├── ejercicio.py  
└── README.md
```
---
### Justificación 
#### Sistema de Caja y Despacho
Se utiliza deque para representar la fila de clientes, siguiendo el patrón FIFO, el primer cliente que llega debe ser el primero en ser atendido

- append() agrega clientes al final de la fila
- popleft() elimina y devuelve al primer cliente de la fila
- Se valida que no se pueda cobrar cuando la fila está vacia

Para la bolsa de productos se utiliza una lista como pila, el último producto guardado debe ser el primero en ser registrado por el cajero.

- append() agrega productos a la bolsa
- pop() elimina y devuelve el ultimo producto ingresado
- se pueden registrar productos cuando la bolsa está vacia

Sets para administrar las membresias y los cupones utilizados durante la sesion

- in permite comprobar si una membresía se encuentra vigente
- add() registra los cupones que ya fueron utilizados
- Un mismo cupon no puede utilizarse mas de una vez durante la sesion


### Obtener repositorio

#### A. (Solo Primera vez)
 Clonar el repositorio localmente:
- HTTP:
```bash
git clone https://github.com/YonaZakkart/estructura_de_datos-practices.git
```
- SSH:
```bash 
git clone git@github.com:YonaZakkart/estructura_de_datos-practices.git
```
Entra a la carpeta de esta practica: 
```bash
cd estructura_de_datos-practices/practice04/
```
#### B. Actualizar localmente
 Si ya tienes el repositorio clonado, actualiza con git pull:
- Entra a la carpeta
```text
estructura_de_datos-practices/
```
- Pull al repositorio
```bash
git pull
```
Entra a la carpeta de esta practica: 
```bash
cd estructura_de_datos-practices/practice04/
```
---
### Ejecutar
Estando en: `estructura_de_datos-practices/practice04/`

- Ejercicio Sistema de Caja y Despacho
```bash
python ejercicio.py
```

___
##### Notas:
- Ya le estoy rntrndiendo a esto de los readme
- noHagoNada no hace nada :b
- Like si estas al borde de la locura o si te gusta el pan