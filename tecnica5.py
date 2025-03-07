def invert_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    return invertida

entrada = input("Digite uma string: ")
print(invert_string(entrada))
