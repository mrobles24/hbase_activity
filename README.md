## COMO EJECUTAR
1. Tener ejecutándose el docker de hbase (en el proyecto hbase ejecutar `./start-hbase.sh`)
2. Colocarnos sobre este proyecto y ejecutar `python3 hbase_activity.py`

## RESULTADO EJECUCIÓN

```bash
Table 'sensor_data' does not exist. Proceeding to create it.
Table 'sensor_data' created.

Tables in HBase: [b'sensor_data']

Inserting data into 'sensor_data' table...

Escaneando todos los datos de la tabla 'sensor_data':
Row key: sensor01_202401010830
Column Family: measurements:humidity
    Column: 60.1
Column Family: measurements:pressure
    Column: 1013.2
Column Family: measurements:temperature
    Column: 22.5
Column Family: meta:location
    Column: Madrid
Column Family: meta:status
    Column: active
Column Family: meta:timestamp
    Column: 2024-01-01 08:30
Column Family: sensor_info:sensor_id
    Column: sensor01
Row key: sensor02_202401010830
Column Family: measurements:humidity
    Column: 58.3
Column Family: measurements:pressure
    Column: 1012.8
Column Family: measurements:temperature
    Column: 20.0
Column Family: meta:location
    Column: Barcelona
Column Family: meta:status
    Column: active
Column Family: meta:timestamp
    Column: 2024-01-01 08:30
Column Family: sensor_info:sensor_id
    Column: sensor02

Querying specific sensor (sensor01_202401010830):
Column Family: measurements:humidity
    Column: 60.1
Column Family: measurements:pressure
    Column: 1013.2
Column Family: measurements:temperature
    Column: 22.5
Column Family: meta:location
    Column: Madrid
Column Family: meta:status
    Column: active
Column Family: meta:timestamp
    Column: 2024-01-01 08:30
Column Family: sensor_info:sensor_id
    Column: sensor01

Querying all values from 'measurements' column family for sensor01_202401010830:
    60.1
    1013.2
    22.5
```

## CUESTIONES

**1. Create the previous table**

El código crea la tabla sensor_data si no existe previamente. El script verifica la existencia de la tabla y la crea con las familias de columnas sensor_info, measurements, y meta.
Esto se indica en el mensaje:
```bash
Table 'sensor_data' created.
```

**2. Make a query about a specific sensor. What type of data is returned?**

Cuando consultas un sensor específico (por ejemplo, sensor01_202401010830), el código devuelve todas las columnas asociadas a esa fila.
El tipo de datos devueltos es un conjunto de pares familia de columna:valor, donde cada columna tiene un valor específico asociado. Ejemplo:

```bash
Column Family: measurements:humidity
    Column: 60.1
Column Family: measurements:pressure
    Column: 1013.2
Column Family: measurements:temperature
    Column: 22.5
Column Family: meta:location
    Column: Madrid
```

**3. Can a specific column:family of a sensor be accessed in the query?**

Sí, se puede acceder a una columna específica dentro de una familia de columnas.
En la consulta a un sensor específico, puedes acceder a los valores de las diferentes familias de columnas, como se muestra en los resultados, donde se consultan columnas específicas dentro de cada familia:
`measurements:humidity`, `measurements:pressure`, `measurements:temperature`, etc.

**4. Can all values from a column:family be retrieved?**

Sí, es posible recuperar todos los valores de una familia de columnas específica.
En el ejemplo, cuando realizamos una consulta para la familia measurements del sensor sensor01_202401010830, obtenemos todos los valores dentro de esa familia:

```bash
Querying all values from 'measurements' column family for sensor01_202401010830:
    60.1
    1013.2
    22.5
```
    
