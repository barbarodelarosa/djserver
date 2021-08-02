
def calcular_imc(peso, talla):
    """[summary]

    Args:
        peso ([float]): [El peso se pone en kilogramos eje.(74)]
        talla ([float]): [La talla se pone en metros eje.(1.74)]

    Returns:
        [result_imc]: [Retorna valor del Indice de masa corporal]
    """
    talla = talla**2
    result_imc = peso / talla
    result_imc = result_imc * 100 / 100
    # result_imc = result_imc * 100) / 100
    return round(result_imc,2)

def calificacion_imc(imc):
    """[summary]

    Args:
        imc ([numero]): [Recibe la calificacion del Indice de masa corporal]

    Returns:
        [string]: [Retorna la calificacion del Indice de masa corporal]
    """
    calificacion = ""
    if imc < 16.00:
        calificacion = "Delgadez severa"
        print(calificacion)
    elif imc >= 16.00 and imc <= 16.99:
        calificacion = "Delgadez moderada"
        print(calificacion)
    elif imc >= 17.00 and imc <= 18.49:
        calificacion = "Delgadez leve"
        print(calificacion)
    elif imc >= 18.50 and imc <= 24.99:
        calificacion = "Normal"
        print(calificacion)
    elif imc >= 25.00 and imc <= 29.99:
        calificacion = "Sobrepeso"
        print(calificacion)
    elif imc >= 30.00 and imc <= 34.99:
        calificacion = "Obesidad leve"
        print(calificacion)
    elif imc >= 35.00 and imc <= 39.99:
        calificacion = "Obesidad media"
        print(calificacion)
    elif imc >= 40:
        calificacion = "Obesidad severa"
        print(calificacion)
    return calificacion