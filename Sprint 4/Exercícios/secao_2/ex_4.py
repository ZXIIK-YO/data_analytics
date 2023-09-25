def calcular_valor_maximo(operadores, operandos) -> float:
    # Verificar se há pelo menos um operador e um operando
    if not operadores or not operandos:
        return float('-inf')  # Retornar valor negativo infinito se não houver operações
    
    # Função para calcular o resultado com base no operador e operandos
    calcular_resultado = lambda op, a, b: {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '%': a % b
    }[op]
    
    # Aplicar a função calcular_resultado usando map e zip
    resultados = map(lambda x: calcular_resultado(*x), zip(operadores, *zip(*operandos)))
    
    # Encontrar o maior valor nos resultados
    max_valor = max(resultados)
    
    return max_valor

# Exemplo de entrada
operadores = ['+','-','*','/','+']
operandos = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

# Calcular o maior valor
maior_valor = calcular_valor_maximo(operadores, operandos)

print("Maior Valor:", maior_valor)
