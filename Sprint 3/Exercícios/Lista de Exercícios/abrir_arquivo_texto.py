# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

try:
    with open('arquivo_texto.txt', 'r') as arquivo:
        # Abre o arquivo de texto "arquivo_texto.txt" em modo de leitura ('r').
        # O 'with' garante que o arquivo será fechado após a leitura.
        # O arquivo é referenciado como 'arquivo'.

        for linha in arquivo:
            # Loop que itera pelas linhas do arquivo.
            # 'linha' recebe cada linha do arquivo em cada iteração.

            print(linha, end='')
            # Imprime a 'linha' atual sem adicionar uma nova linha após cada linha lida.
            # O 'end=' evita a quebra de linha adicional.

except FileNotFoundError:
    # Trata a exceção 'FileNotFoundError', que ocorre se o arquivo não for encontrado.
    print("O arquivo 'arquivo_texto.txt' não foi encontrado.")

except Exception as e:
    # Trata qualquer outra exceção genérica que possa ocorrer durante a execução.
    # 'e' é uma variável que armazena informações sobre a exceção.
    print(f"Ocorreu um erro: {e}")
