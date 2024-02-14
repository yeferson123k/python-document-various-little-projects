def main():
    user_response = input('Write a word: ')
    # Si deseas recorrer la palabra puedes hacer esto
    for char in user_response: # los strings son iterables
        print(char)
    """Output
    Write a word: hello world
    h
    e
    l
    l
    o

    w
    o
    r
    l
    d"""
    # Si lo que desea es simplemente obtener el arreglo para procesarlo o lo que sea puedes hacer lo siguiente:
    word_chars = list(user_response)
    print(word_chars)
    """Output
    Write a word: hi
    ['h', 'i']"""

if __name__ == '__main__':
    main()

"""en python, las palabras son simplemente listas de Strings. es decir, si haces palabra = "agua", ya puedes separarla letra por letra, pues ya es de la forma ["a", "g", "u", "a"], solo que lo muestra todo junto porque en primera instancia lo toma como String.

como prueba, puedes correr esto en python:"""

palabra = "agua"
print(palabra[0])
print(palabra[1])
print(palabra[2])
print(palabra[3])
"""es decir, declaramos un string ("agua") pero inmediatamente ya se podía leer como lista.

por lo que lo único que debes hacer, es decirle a python que en vez de tomarlo como String, que lo tome como lista."""

palabra = "agua"
palabra = list(palabra)
print(palabra)
"""Espero esto te sirva y hayas aprendido un poco más ;)"""