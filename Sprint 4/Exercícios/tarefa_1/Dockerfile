# Use a imagem base do Python
FROM python:3.8

# Copie o arquivo carguru.py para o diretório de trabalho no container
COPY carguru.py /app/carguru.py

# Defina o diretório de trabalho como /app
WORKDIR /app

# Execute o arquivo carguru.py quando o container for iniciado
CMD ["python", "carguru.py"]
