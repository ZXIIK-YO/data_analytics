from functools import reduce

def calcula_saldo(lancamentos) -> float:
    # Função lambda para mapear os lançamentos para seus valores com o sinal correto
    mapear_valor = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]
    
    # Usar map para aplicar a função de mapeamento a cada lançamento
    valores = map(mapear_valor, lancamentos)
    
    # Usar reduce para somar os valores e calcular o saldo final
    saldo_final = reduce(lambda x, y: x + y, valores, 0.0)
    
    return saldo_final

# Exemplo de entrada
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

# Calcular o saldo
saldo_final = calcula_saldo(lancamentos)

print("Saldo Final:", saldo_final)
