import psycopg2

conexion = psycopg2.connect(user="postgres",
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
query = 'SELECT * FROM persona WHERE id_persona = 1'
cursor.execute(query)
resultado_query = cursor.fetchall()
print(resultado_query)
cursor.close()
conexion.close()