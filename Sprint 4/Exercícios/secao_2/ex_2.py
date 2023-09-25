def conta_vogais(texto:str)-> int:
     # Função lambda para verificar se um caractere é uma vogal
    is_vogal = lambda char: char in 'aeiouAEIOU'
    
    # Converte a string para minúsculas e filtra os caracteres que são vogais
    vogais = filter(is_vogal, texto.lower())
    
    # Retorna o comprimento (contagem) das vogais
    return len(list(vogais))

# Exemplo de uso:
texto = "Olá, mundo!"
resultado = conta_vogais(texto)
print(resultado)  # Deve imprimir 3