# Código executado para obter a contagem das palavras no notebook

from pyspark.sql import SparkSession

# Inicialize a sessão Spark
spark = SparkSession.builder.appName("Contagem de Palavras").getOrCreate()

# Carregue o conteúdo do arquivo README.md
file_path = "file:/home/jovyan/work/README.md"  # ajuste o caminho aqui
text_rdd = spark.sparkContext.textFile(file_path)

# Divida as linhas em palavras e conte as ocorrências de cada palavra
word_counts = text_rdd.flatMap(lambda line: line.split(" ")).countByValue()

# Exiba a contagem de palavras
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Encerre a sessão Spark
spark.stop()
