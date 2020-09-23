import psycopg2 as db

conexion = db.connect(user="postgres",
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
query = 'SELECT * FROM persona WHERE id_persona = %s'
#id_persona = 2
id_persona = input("Proporciona la pk a buscar:")
llave_primaria = (id_persona,)
cursor.execute(query,llave_primaria)
resultado_query = cursor.fetchall()
print(resultado_query)
cursor.close()
conexion.close()