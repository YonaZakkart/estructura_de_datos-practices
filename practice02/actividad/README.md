## Practica 2: Estructuras de Datos en Python (`list`, `tuple`, `set`)

Esta carpeta contiene una serie de ejercicios sobre los tipos de datos vistos

### Estructura del Proyecto

```text
.
├── listas
|   ├── historial_navegacion.py 
|   └── lista_reproduccion.py
├── set
|   ├── etiquetas_catalogo.py
|   └── registro_asistencia.py
├── tuplas  
|   ├──app_config.py
|   └──coordenadas.py
├── biblioteca.py   
└── README.md
```
---
### Justificación 
#### Listas 
Ordenadas, mutables, permiten duplicados
- Playlist de musica: necesita mantener un orden en la cola, agregar/quitar elementos y permitir canciones repetidas.
- Historial de navegación: comportamiento de una pila donde la URL más reciente ingresa al final con .append() y se retrocede con .pop().

#### Set
No ordenados, mutables, elementos unicos, búsqueda.
- Registro de asistencia: Elimina automáticamente duplicados cuando un usuario intenta registrarse mas de una vez
- Etiquetas de catalogo: Facilita operaciones matematicas de conjuntos (& intersección, - diferencia, | unión) para comparar tags de productos en un e-commerce.

#### Tuplas 
Ordenadas, inmutables, eficientes en memoria.Caso de uso en scripts (03 y 04):
- Coordenadas GPS: La latitud, longitud y altitud representan un registro fijo que no debe modificarse
- Configuración de app: Parametros como servidor, puerto y protocolo se fijan al arrancar y deben ser de solo lectura para evitar errores

### Ejercicio adicional
#### biblioteca.py
Muestra como conviven los tres tipos de datos en un solo contexto:
- tupla: Modela los libros como registros inmutables (ID, Titulo, Autor) 
- set: Mantiene los ID prestados actualmente, garantizando unicidad 
- list: Registra el historial de transacciones en orden cronologico. 
---
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
cd estructura_de_datos-practices/practice02/actividad/
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
cd estructura_de_datos-practices/practice02/actividad/
```
---
### Ejecutar
Estando en: `estructura_de_datos-practices/practice02/actividad/`

- Ejercicios de Listas
```bash
python listas/historial_navegacion.py
```
```bash
python listas/lista_reproduccion.py
```
- Ejercicios de Sets
```bash
python listas/etiquetas_catalogo.py
```
```bash
python listas/registro_asistencia.py
```
- Ejercicios de Tuplas
```bash
python listas/app_config.py
```
```bash
python listas/coordenadas.py
```
- Ejercicio adicional: Biblioteca
```bash
python biblioteca.py
```
___
##### Notas:
- Separe los ejercicios dependiendo del tipo (mas trabajo)
- Hice un ejercicio donde estan presentes los 3 tipos de datos vistos (aunque no se pidio)
- Estoy aprendiendo a hacer los Readme (me tarde mas en esto que en los ejercicios)
- en historial_navegacion.py hay 2 url de repositorios de jueguitos que he estado haciendo (uno con 95% IA y el otro con 5% IA)
- Like si estas al borde de la locura o si te gusta el pan