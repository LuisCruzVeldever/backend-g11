def sumar(num1, num2):
    return num1 + num2
resultado = sumar(1,2)
print (resultado)

resultado2 = sumar(num1=1, num2=2)

parametros = {

    'num1': 5,
    'num2': 8
}

resultado3 = sumar(num1 = parametros.get('num1'), num2 = parametros.get('num2')
print(resultado3)