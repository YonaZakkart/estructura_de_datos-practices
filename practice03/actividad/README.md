## Practica 3: Patrones LIFO, FIFO y Álgebra de Conjuntos

Esta carpeta contiene una serie de ejercicios de la practica 3. Abordando los métodos integrados de Listas y Sets en Python, los patrones LIFO (Pilas), FIFO (Colas) y el álgebra de conjuntos

### Estructura del Proyecto

```text
.
├── 01_cola_clientes.py
├── 02_validacion_permisos.py   
└── README.md
```
---
### Justificación 
#### Ejercicio 01
Se utiliza FIFO porque el primer cliente que llega es el primero que debe ser atendido
- append() agrega clientes a la cola.
- popleft() elimina al primer cliente de la cola.

#### Ejercicio 02
Se utiliza un set porque los permisos no deben repetirse y es facil compararlos
- issubset() comprueba si el usuario tiene todos los permisos necesarios.
- encuentra los permisos que le faltan.

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
cd estructura_de_datos-practices/practice03/actividad/
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
cd estructura_de_datos-practices/practice03/actividad/
```
---
### Ejecutar
Estando en: `estructura_de_datos-practices/practice03/actividad/`

- Ejercicio 01
```bash
python 01_cola_clientes.py
```
- Ejercicio 02
```bash
python 02_validacion_permisos.py
```

___
##### Notas:
- Like si estas al borde de la locura o si te gusta el pan