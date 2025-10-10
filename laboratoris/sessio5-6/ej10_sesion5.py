def es_palindromo(string):
    return string == string[::-1]
print(f"{"Es" if es_palindromo(input("Introduce una palabra: ")) else "NO es"} palíndromo")