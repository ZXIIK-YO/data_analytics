# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json

# Abre o arquivo JSON para leitura
try:
    with open('person.json', 'r') as arquivo:
        # Faz o parsing do conteúdo do arquivo JSON em modo de leitura ('r')
        dados = json.load(arquivo)

        # Imprime os dados em formato legível
        print(dados)

except FileNotFoundError:
    print("O arquivo 'person.json' não foi encontrado.")
except json.JSONDecodeError as e:
    print(f"Erro de parsing JSON: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
