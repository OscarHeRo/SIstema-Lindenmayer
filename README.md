# Sistema L con Turtle

Este es un programa que implementa sistemas L (L-Systems) utilizando la biblioteca Turtle de Python. Los sistemas L son gramáticas formales utilizadas para modelar el crecimiento de estructuras biológicas, como plantas, y también tienen aplicaciones en gráficos por computadora y arte generativo.

## Gramática del Sistema L

En este programa, la gramática del sistema L se define mediante un conjunto de reglas de producción. Cada regla especifica cómo se reemplazan los símbolos en la cadena de entrada en cada iteración. La gramática incluye los siguientes símbolos y sus significados:

- `F`: Avanza la tortuga dibujando una línea.
- `+`: Gira la tortuga hacia la izquierda en un ángulo especificado.
- `-`: Gira la tortuga hacia la derecha en un ángulo especificado.
- `[`: Guarda la posición y la orientación de la tortuga en una pila.
- `]`: Recupera la última posición y orientación de la tortuga desde la pila.

## Implementación

El programa consta de varias partes:

1. **Clase LSystem**: Define un sistema L con un axioma inicial y reglas de producción.
2. **Función draw_lsystem**: Utiliza la biblioteca Turtle para dibujar las instrucciones generadas por el sistema L.
3. **Función main**: Configura la ventana de Turtle y genera las instrucciones del sistema L para su dibujo.
4. **Función get_user_input**: Permite al usuario personalizar el sistema L proporcionando un axioma, reglas de producción y ángulo de giro.
5. **Función select_example**: Proporciona ejemplos predeterminados para que el usuario elija y dibuje.

## Cómo usar el programa

Para ejecutar el programa, simplemente ejecuta el archivo Python `main.py`. Esto abrirá una ventana donde podrás seleccionar un ejemplo predeterminado o personalizar tu propio sistema L.

Si eliges personalizar, se te pedirá que ingreses un axioma, una regla de producción para el símbolo `F` y un ángulo de giro. Una vez que completes la entrada, haz clic en el botón "Dibujar" y se generará y dibujará el sistema L.

¡Disfruta explorando la belleza de los sistemas L con Turtle!
