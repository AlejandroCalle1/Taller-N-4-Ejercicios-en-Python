def encontrar(cadena1, cadena2):
    if len(cadena1) != len(cadena2):
        return "Las cadenas deben ser de la misma longitud"
    
    diferencias = [] 
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:  
            diferencias.append(cadena2[i])  
    
    return diferencias

print(encontrar("Me llamo mouredev", "Me llamo mouredov"))  
print(encontrar("Me llamo.Brais Moure", "Me llamo brais moure")) 
