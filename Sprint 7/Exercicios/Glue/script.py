import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as f

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = "s3://zxii-lab-glue"

dynamic_df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","},
)

spark_df = dynamic_df.toDF()

# Imprima o schema do dataframe
print("Schema do dataframe:")
spark_df.printSchema()

# Altere a caixa dos valores da coluna nome para MAIÚSCULO
spark_df = spark_df.withColumn("nome", f.upper(f.col("nome")))

# Imprima a contagem de linhas no dataframe
print("Contagem de linhas:", spark_df.count())

# Imprima a contagem de nomes agrupados por ano e sexo
print("Contagem de nomes por ano e sexo:")
spark_df.groupBy("ano", "sexo").count().show()

# Ordene os dados pelo ano de forma decrescente
spark_df = spark_df.orderBy("ano", ascending=False)

# Nome feminino com mais registros e em que ano ocorreu
max_female_name = spark_df.filter(spark_df["sexo"] == "F").groupBy("nome", "ano").count().orderBy("count", ascending=False).first()
print("Nome feminino com mais registros:", max_female_name['nome'], "em", max_female_name['ano'])

# Considerar apenas as primeiras 10 linhas
spark_df.show(10)

# Escreva o conteúdo do dataframe no S3
output_path = target_path + "/frequencia_registro_nomes_eua"
spark_df.write.partitionBy("sexo", "ano").json(output_path)

job.commit()
