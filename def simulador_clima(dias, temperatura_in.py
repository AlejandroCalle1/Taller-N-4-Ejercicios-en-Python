import random
def simulador_clima(dias, temperatura_inicial):
    temperatura = temperatura_inicial
    dias_lluviosos = 0
    temp_max = temperatura
    temp_min = temperatura
    llovio_dia_anterior = False  

    print("Día | Temp (°C) | Lluvia")
   
    for dia in range(1, dias + 1):
        if llovio_dia_anterior:  
            temperatura -= 1

        if temperatura > 25:  
            llueve = True
            dias_lluviosos += 1
            temperatura -= 1  
        elif temperatura < 5:  
            llueve = False
        else:
            # Lluvia aleatoria si la temperatura está entre 5°C y 25°C
            llueve = random.choice([True, False])  # Decide aleatoriamente si llueve
            if llueve:
                dias_lluviosos += 1

        llovio_dia_anterior = llueve  
        
        temp_max = max(temp_max, temperatura)
        temp_min = min(temp_min, temperatura)

        print(dia,temperatura, llueve )
   
    print("Máxima:", temp_max,"°C","Mínima: ", temp_min ,"°C", "Días lluviosos:" ,dias_lluviosos)

simulador_clima(dias=10, temperatura_inicial=10)
