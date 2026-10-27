
# Análisis Batch de Inventarios y Logística con Apache Spark

## 1. Descripción del proyecto

Este proyecto desarrolla un análisis de datos por lotes (Batch) mediante Apache Spark y Python, utilizando DataFrames para procesar información de inventarios y operaciones logísticas.

El propósito es obtener indicadores que apoyen la gestión de inventarios, la evaluación de proveedores y el seguimiento de pedidos en una organización.

## 2. Conjunto de datos

Nombre: Inventory Supply Chain Dataset

Fuente pública:
https://github.com/nikhilsabban/supplychain_analysis

Archivo: Inventory_SupplyChain_Dataset.csv

El conjunto de datos contiene 1.200 registros y 15 columnas relacionadas con:

- Categorías de productos.
- Unidades vendidas.
- Niveles de inventario.
- Proveedores y almacenes.
- Tiempos de entrega.
- Costos de transporte.
- Estados de los pedidos.
- Pedidos con condición de backorder.

Los datos se utilizan con fines académicos.

## 3. Tecnologías utilizadas

- Apache Spark 3.5.8.
- Python 3.10.
- PySpark.
- Ubuntu.
- PuTTY para acceder a la máquina virtual.

## 4. Procesamiento realizado

### Carga de datos

El archivo CSV se carga mediante Spark DataFrames, utilizando las opciones header=True e inferSchema=True.

### Calidad y limpieza

Se realizaron las siguientes verificaciones:

- Total de registros: 1.200.
- Total de columnas: 15.
- Valores nulos detectados: 0.
- Filas completamente duplicadas: 0.

Se utiliza dropDuplicates() para obtener un DataFrame sin filas duplicadas. No fue necesario eliminar registros por valores nulos.

### Transformación y análisis exploratorio

Se realizaron seis análisis:

1. Unidades vendidas e inventarios registrados por categoría.
2. Tiempo promedio de entrega por proveedor.
3. Cantidad de registros con y sin backorder.
4. Costo promedio de transporte por región.
5. Distribución de los estados de los pedidos.
6. Relación entre los estados de los pedidos y backorder.

Las operaciones se desarrollaron utilizando groupBy(), agg(), sum(), avg() y count().

## 5. Resultados principales

- La categoría Ropa registró 168.642 unidades vendidas.
- El proveedor A presentó el menor tiempo promedio de entrega, aproximadamente 15,23 días.
- Se identificaron 116 registros con backorder, equivalentes al 9,67 %.
- La región Este presentó el mayor costo promedio de transporte, aproximadamente 7.977,15 unidades monetarias.
- Se encontraron 838 registros de pedidos cumplidos, 248 pendientes y 114 cancelados.

Estos resultados corresponden al conjunto de datos analizado y no representan necesariamente indicadores actuales de una empresa real.

## 6. Instrucciones de ejecución

Requisitos:

- Python 3.
- Apache Spark con soporte para PySpark.
- Java compatible con la versión de Spark utilizada.

Ubicar los siguientes archivos en una misma carpeta:

- analisis_batch.py
- Inventory_SupplyChain_Dataset.csv

Abrir una terminal en esa carpeta y ejecutar:

    spark-submit analisis_batch.py

El programa mostrará los resultados en la terminal y generará seis carpetas de salida dentro del directorio resultados/.

Cada carpeta contiene archivos CSV generados por Spark con los indicadores correspondientes.

## 7. Visualización

Los resultados se presentan mediante tablas en la consola de Spark y archivos CSV de salida, que pueden consultarse para interpretar los indicadores.

## 8. Conclusiones

Apache Spark permitió procesar el conjunto de datos mediante operaciones de carga, verificación de calidad, transformación y análisis exploratorio.

Los indicadores obtenidos permiten comparar el comportamiento de las ventas, los inventarios, los tiempos de entrega y los costos logísticos.

El procesamiento Batch constituye una herramienta útil para apoyar el análisis de información y la toma de decisiones en el ámbito de la Ingeniería Industrial.

## 9. Autora

Yeny Paola Becerra Castro

Programa de Ingeniería Industrial
Universidad Nacional Abierta y a Distancia (UNAD)

Actividad académica: Tarea 3 - Big Data
