
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when, sum, avg, round

# 1. Iniciar Apache Spark
spark = SparkSession.builder \
    .appName("Analisis_Batch_Inventarios") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Cargar el conjunto de datos
df = spark.read.csv(
    "Inventory_SupplyChain_Dataset.csv",
    header=True,
    inferSchema=True
)

print("\n=== CONJUNTO DE DATOS ===")
print("Total de registros:", df.count())
print("Total de columnas:", len(df.columns))
df.printSchema()

# 3. Verificar la calidad de los datos
print("\n=== VALORES NULOS ===")
df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
]).show(truncate=False)

duplicados = df.count() - df.dropDuplicates().count()
print("Registros duplicados:", duplicados)

# 4. Limpieza y transformacion
# Se eliminan duplicados si existen.
# No se eliminan nulos sin revisar su significado.
df_limpio = df.dropDuplicates()

# 5. Analisis exploratorio de datos
analisis = [
    (
        "ventas_inventarios_categoria",
        df_limpio.groupBy("Category").agg(
            sum("Units Sold").alias("Total_Unidades_Vendidas"),
            sum("Inventory Level").alias("Suma_Inventarios_Registrados")
        )
    ),
    (
        "tiempos_entrega_proveedor",
        df_limpio.groupBy("Supplier").agg(
            round(avg("Lead Time (Days)"), 2).alias("Promedio_Dias_Entrega")
        )
    ),
    (
        "pedidos_backorder",
        df_limpio.groupBy("Backorder").count()
    ),
    (
        "costos_transporte_region",
        df_limpio.groupBy("Region").agg(
            round(avg("Transportation Cost"), 2).alias("Costo_Promedio")
        )
    ),
    (
        "estados_pedidos",
        df_limpio.groupBy("Order Status").count()
    ),
    (
        "estados_y_backorder",
        df_limpio.groupBy("Order Status", "Backorder").count()
    )
]

# 6. Visualizar y guardar resultados
for nombre, resultado in analisis:
    print("\n=== " + nombre.upper() + " ===")
    resultado.show(truncate=False)

    resultado.coalesce(1).write \
        .mode("overwrite") \
        .option("header", True) \
        .csv("resultados/" + nombre)

print("\nAnalisis Batch finalizado correctamente.")
print("Resultados guardados en la carpeta resultados/")

spark.stop()
