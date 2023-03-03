<!-- INSTRUCTIONS -->
## Instructions
Dado un string, crear una función CodelandUsernameValidation(str) que determine si un nombre es
válido de acuerdo a las siguientes reglas:
1. El nombre de usuario tiene entre 4 y 25 caracteres.
2. Debe comenzar con una letra.
3. Solo puede contener letras, números y el carácter de subrayado.
4. No puede terminar con un carácter de subrayado.
Si el nombre de usuario es válido, su programa debe devolver la cadena verdadera, de lo
contrario, devolver la cadena falsa.
Agregar un input que permita ingresar la palabra de entrada y una sección que muestra si el texto
es válido o no.
Ejemplos de uso:
• Entrada: "aa_"
• Salida: falso
• Entrada: "u__hello_world123"
• Salida: verdadero
Consideraciones:
- Puedes desarrollar el algoritmo en el lenguaje que quieras.
- El código debe estar en inglés.
- Si debes asumir algo, déjalo por escrito como comentario en el código.
Entregables:
- Un código que implementa el algoritmo.
- Debe crear un README.md con las instrucciones para ejecutar el código.
- Suma puntos si está alojado en github
A Evaluar:
- Correctitud: el algoritmo debe funcionar correctamente.
- Eficiencia: el algoritmo debe ser eficiente.
- Diseño: el código debe ser limpio y fácil de leer.

<!-- MY COMMENTS -->
### my comments
1) Cambié el nombre de la función CodelandUsernameValidation por codeland_username_validation para ajustarse a los nombres de funciones de python.

2) Hice un primer algoritmo estático, que está en first_solution.py
y luego una segunda solución, también estática y más dividida, que está en second_solution.py 
y finalmente una tercera solución, dinámica, que pregunta por "Your word:" al usuario

<!-- RUNNING THE CODE -->
### to run the code
Ejecutar en consola:
    ```
    python3 <nombre archivo python>
    ```
en este caso:
    ```
    python3 third_solution.py
    ```

o las versiones anteriores, si así lo desea:
    ```
    python3 first_solution.py
    ```
    ```
    python3 second_solution.py
    ```
