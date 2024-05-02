# OPERADORES LOGICOS

Los operadores lógicos en Python se utilizan para combinar expresiones booleanas y realizar operaciones de lógica booleana. Estos operadores son and, or y not. Aquí tienes una explicación breve de cada uno junto con tres ejemplos:

`and (y):` Este operador devuelve True si ambas expresiones booleanas evaluadas son verdaderas, de lo contrario, devuelve False.

`or (o):` 
Devuelve True si al menos una de las expresiones booleanas evaluadas es verdadera, de lo contrario, devuelve False.

`not (no):` 
Este operador devuelve el valor contrario de la expresión booleana. Si la expresión es True, not la convierte en False, y viceversa.

## Ejemplos:

1.-Operador and (y):

``` PYTHON
x = 5
y = 10

# Verifica si x es mayor que 3 y y es menor que 15
if x > 3 and y < 15:
    print("Ambas condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")
```

2.- Operador or (o):

```PYTHON
nombre = "Juan"
edad = 25

# Verifica si el nombre es "Juan" o la edad es mayor que 30
if nombre == "Juan" or edad > 30:
    print("Una de las condiciones es verdadera.")
else:
    print("Ambas condiciones son falsas.")
```
3.- Operador not (no):

``` PYTHON
llueve = True

# Verifica si no está lloviendo
if not llueve:
    print("No está lloviendo.")
else:
    print("Está lloviendo.")
```
En cada ejemplo, los operadores lógicos se utilizan para combinar expresiones booleanas y tomar decisiones basadas en el resultado de esas combinaciones.

