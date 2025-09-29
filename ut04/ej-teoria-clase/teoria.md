# Teoria Python Clase

## else.py

```python
num = input("Dime un numero: ")
if ( int(num)%2 == 0 ):
    print("Es par")
else:
    print("Es impar")

#Ejemplo de comentario.
```

## hola.py
```python
print("Hola mundo")
```

## if.py
```python
saludar = True
if ( saludar ):
    nombre = "Victor"
    print(f"Hola {nombre}")
print("Adios")
```

## ifanidados.py
```python
num = input("Dime un numero: ")
if ( not num.isdigit() ):
    print("El valor que has introducido no es un numero")
elif (int(num)%2 == 0):
    print("El numero es par")
else:
    print("El numero es impar")
```

## ifternario.py
```python
edad = int( input("Dime tu edad: ") )
msg = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(msg)
```

## ifternarioanidado.py
```python
edad = int( input("Dime tu edad: ") )
msg = (
    "Adulto" if edad >= 18 else 
    "Adolescente" if edad >= 13 else 
    "Niño"
    )
print(msg)
```