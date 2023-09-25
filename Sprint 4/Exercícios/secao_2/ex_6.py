def maiores_que_media(conteudo: dict) -> list:
    # Calcula a média dos preços dos produtos
    valores = list(conteudo.values())
    media = sum(valores) / len(valores)

    # Filtra os produtos cujo valor é superior à média
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]

    # Ordena a lista pelo preço em ordem crescente
    produtos_acima_media.sort(key=lambda x: x[1])

    return produtos_acima_media
