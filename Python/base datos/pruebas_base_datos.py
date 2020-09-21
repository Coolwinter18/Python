import psycopg2

conexion = psycopg2.connect(user="postgres",
                 password='1234',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
query = 'SELECT * FROM persona'
cursor.execute(query)
resultado_query = cursor.fetchall()
print(resultado_query)
cursor.close()
conexion.close()