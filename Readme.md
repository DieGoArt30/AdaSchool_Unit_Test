## Reto Curso Django - Ada School

Reto tomado de [wix/tdd-katas](https://github.com/wix/tdd-katas#readme)

## Greeter

#### Antes de comenzar:
* **Trata de no leer más allá.**
* **Realiza una tarea a la vez. El truco está en aprender a trabajar incrementalmente.**

Esta kata demuestra los problemas de las funciones y objetos con alcance estático.

Todos los tests siempre deben pasar, independientemente de las condiciones del entorno.

1. Escribe una clase `Greeter` con una función `greet` que recibe un `nombre` como entrada y muestra `Hola <nombre>`. La firma de `greet` no debe cambiar a lo largo de la kata. Se te permite construir el objeto `Greeter` como prefieras.
2. `greet` elimina los espacios en blanco alrededor del nombre.
3. `greet` capitaliza la primera letra del nombre.
4. `greet` devuelve `Buenos días <nombre>` cuando la hora es de 06:00 a 12:00.
5. `greet` devuelve `Buenas tardes <nombre>` cuando la hora es de 18:00 a 22:00.
6. `greet` devuelve `Buenas noches <nombre>` cuando la hora es de 22:00 a 06:00.
7. `greet` registra en la consola cada vez que es llamado.
