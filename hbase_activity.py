import happybase
from datetime import datetime

# Conectar a HBase en el puerto Thrift
connection = happybase.Connection('127.0.0.1', 32807) 

# Verificamos si la tabla 'sensor_data' ya existe, si no, la creamos
if 'sensor_data' not in connection.tables():
    print("Table 'sensor_data' does not exist. Proceeding to create it.")
    connection.create_table(
        'sensor_data',
        {
            'sensor_info': dict(),
            'measurements': dict(),
            'meta': dict()
        }
    )
    print("Table 'sensor_data' created.")
else:
    print("Table 'sensor_data' already exists.")

# Mostramos todas las tablas existentes
print("\nTables in HBase:", connection.tables())

# Nos conectamos a la tabla 'sensor_data'
table = connection.table('sensor_data')

# Insertamos los datos
print("\nInserting data into 'sensor_data' table...")
table.put('sensor01_202401010830', {
    'sensor_info:sensor_id': 'sensor01',
    'measurements:temperature': '22.5',
    'measurements:humidity': '60.1',
    'measurements:pressure': '1013.2',
    'meta:timestamp': '2024-01-01 08:30',
    'meta:location': 'Madrid',
    'meta:status': 'active'
})

table.put('sensor02_202401010830', {
    'sensor_info:sensor_id': 'sensor02',
    'measurements:temperature': '20.0',
    'measurements:humidity': '58.3',
    'measurements:pressure': '1012.8',
    'meta:timestamp': '2024-01-01 08:30',
    'meta:location': 'Barcelona',
    'meta:status': 'active'
})

# Mostramos todos los datos de la tabla (escaneo completo)
print("\nEscaneando todos los datos de la tabla 'sensor_data':")
for k, data in table.scan():
    print(f"Row key: {k.decode('utf-8')}")
    for family, columns in data.items():
        print(f"Column Family: {family.decode('utf-8')}")
        if isinstance(columns, bytes):
            # Si columns es un objeto bytes, lo decodificamos para que sea legible
            print(f"    Column: {columns.decode('utf-8')}")
        else:
            for column, value in columns.items():
                print(f"    {column.decode('utf-8')}: {value.decode('utf-8')}")

# Consulta para un sensor específico (sensor01_202401010830)
print("\nQuerying specific sensor (sensor01_202401010830):")
sensor_row = table.row('sensor01_202401010830'.encode('utf-8'))
for family, columns in sensor_row.items():
    print(f"Column Family: {family.decode('utf-8')}")
    if isinstance(columns, bytes):
        # Si columns es un objeto bytes, lo decodificamos para que sea legible
        print(f"    Column: {columns.decode('utf-8')}")
    else:
        for column, value in columns.items():
            print(f"    {column.decode('utf-8')}: {value.decode('utf-8')}")

# Consultamos todos los valores de la columna 'measurements' para un sensor específico
print("\nQuerying all values from 'measurements' column family for sensor01_202401010830:")
sensor_measurements = table.cells('sensor01_202401010830'.encode('utf-8'), 'measurements')
for value in sensor_measurements:
    print(f"    {value.decode('utf-8')}")
