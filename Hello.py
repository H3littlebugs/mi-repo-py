from datetime import datetime

def años_restantes(hasta_año):
    # Obtener el año actual
    año_actual = datetime.now().year

    # Calcular los años restantes
    años_restantes = hasta_año - año_actual

    return años_restantes

# Definir el año objetivo
año_objetivo = 2035

# Llamar a la función y mostrar el resultado
años_restantes_2024 = años_restantes(año_objetivo)
print(f"Años restantes hasta el año {año_objetivo}: {años_restantes_2024}")


