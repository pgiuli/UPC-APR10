# Introducció al codi Python

## La terminal de Python

En ser un llenguatge compilat en temps real (JIT Compiling) tenim 
l'oportunitat d'executar qualsevol instrucció directament en una terminal de Python dins un espai de memòria propi.

## Redacció d'un programa en un fitxer (cas habitual)

Com és evident, no és gens pràctic haver d'escriure manualment totes les instruccions d'un programa en la terminal cada cop que el volem executar o realitzar un petit canvi. Per això definirem les instruccions legals en un arxiu `.py` que executarem des de l'IDE o amb `python programa.py`

## Depuració del programa

Podem inserir punts de parada (breakpoints) entre instruccions dins el nostre editor per tal d'observar l'assignació de valors i el canvi de les variables dins un programa més complex per tal de solventar problemes derivats d'errors en l'algoritme o la redacció del programa

## Característiques del llenguatge

Python ens inclou, entre d'altres:

 - Estructures de dades eficients i d'alt nivell
 - Simplicitat d'enfoc però efectiu en OOP.

 - Desenvolupament ràpid i amb portabilitat en moltes plataformes

 - Modularitat: inclou moduls estàndards per la resolució de problemes i la interacció amb l'entorn de l'usuari.


## Variables

Noms que refereixen un valor o objecte.
Mitjançant la seva declaració es crea aquesta i se l'assigna un valor.
`num = 12`,  `frase = "Hola!"`
Sempre és del nostre interès assignar-li un nom representatiu i clar.
Cada variable té el seu _tipus_ que es pot trobar amb `type(num) -> int` però no cal especificar-lo a l'hora de la declaració.

Normes:
 - Lletres, nombres i _
 - Ha de començar per una lletra
 - No poden coincidir amb un mètode propi `keyword.kwlist`

### Tipus de dades bàsics
#### Enters
    - int (32 bit)
    - long
#### Reals
    - floats
    - double (major precisió de coma flotant)

#### Conversions - Casting (sempre entre valors compatibles)
```
x = 3
y = float(x)
enter = int(3.2)
```

#### Boolean: representació binària en la forma dels valors `True` i `False`.

#### Nombres complexos (tret característic del llenguatge)
Es poden definir a partir de la redacció directa del nombre amb `c1 = 3+2k` o amb la funció `complex` que empra dos arguments (part real i imaginària) `c2 = complex(3, -2)`.

Els nombres complexos tenen tenen mètodes com: `c1.conjugate()` (no modifica el nombre, sinó que retorna el conjugat) i atributs com `c1.real`i `c2.imag`.

#### Constants: declarades amb un nom en majúscules.

#### Expressions: combinen objectes i operadors.


### Operacions matemàtiques
- Suma `+`
- Resta `-`
- Multiplicació `*`
- Divisió `/`
- Quiocient div. `//`
- Mòdul (resta): `%`
- Potència `**`

### Operacions relacionals
- Menor que `<`
- Menor o igual que `<=``
- Major que `>`
- Major o igual que `>=``
- Igual `==`
- Diferent `!=`

### Operadors lògics
- i/AND `and`
- o/OR `or`
- negació/NOT `not``


## Sentències i instruccions bàsiques

### Entrada
Lectura del teclat: `nom = input()`. Pot inclore un argument per a mostrar un text durant la lectura `pes = input("Introdueix el teu pes:")`

Cal recordar la importància de convertir el tipus de la variable obtinguda ja que aquesta funció sempre retornarà un `str`.

### Sortida
Escritura en pantalla: `print(variable)`. Aquesta funció pot rebre tants arguments com es vulgui (separats per una coma, evidentment.) i els concadenarà a l'hora de fer la impressió a la terminal.

`print("El conjugat de", 3+3j, "és:", 3+3j.conjugate()) -> (3-3j)`

#### Sidenote: f-strings

Es poden combinar variables dins un string en posicions especificades d'aquesta manera:
```
val1 = 2
val2 = 3
suma = val1 + val2
print(f"El valor de la suma de {val1} i {val2} és: {suma}.")
```

### Condicionals
### Iteratives

## Objectes

Exemples: nombre senters, persones, vehicles, arxius...