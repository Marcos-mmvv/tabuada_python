def calcular_tabuada(x, y):
    soma = x + y
    yield soma
    subtração = x - y
    yield subtração
    mutiplicacao = x * y
    yield mutiplicacao
    divisao = x / y
    yield divisao

# Programa principal

x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))

#Exibe os resultados
resultados = calcular_tabuada(x, y)

#Usando laço de repetição FOR
#for resultado in resultados:
    #print(resultado)

print(f' A soma é {next(resultados)}')
print(f' A subtração é {next(resultados)}')
print(f' A multiplicação é {next(resultados)}')
print(f' A divisão é {next(resultados)}')

