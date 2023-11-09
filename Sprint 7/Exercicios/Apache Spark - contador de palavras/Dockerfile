# Use a imagem jupyter/all-spark-notebook como imagem base
FROM jupyter/all-spark-notebook

# Baixe o arquivo README.md diretamente para o contêiner
RUN wget -O /home/jovyan/work/README.md "https://raw.githubusercontent.com/ZXIIK-YO/data_analytics/master/README.md?token=GHSAT0AAAAAACGTZ3WLD2HFW67AZKGL5AB2ZKL5BCQ"

# Expõe a porta 8888
EXPOSE 8888
