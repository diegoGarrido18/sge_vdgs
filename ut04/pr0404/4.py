def invertir_diccionario(dic):
    # Creamos un nuevo diccionario
    dic_invertido = {}
    for clave, valor in dic.items():
        # Intercambiamos clave y valor
        dic_invertido[valor] = clave
    return dic_invertido

# Ejemplo
mi_dic = {'a': 1, 'b': 2, 'c': 3}
dic_invertido = invertir_diccionario(mi_dic)
print(dic_invertido)
