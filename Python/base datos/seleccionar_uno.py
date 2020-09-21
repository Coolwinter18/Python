import psycopg2 as db

conexion = db.connect(user="postgres",
                 password='1234',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
query2 = 'DELETE FROM persona WHERE id_persona > 2'
query = 'SELECT * FROM persona WHERE id_persona = %s'
id_persona = 3 #input("Proporciona la pk a buscar:")
llave_primaria = (id_persona,)
cursor.execute(query2)
cursor.execute(query,llave_primaria)

resultado_query = cursor.fetchall()
print(resultado_query)
cursor.close()
conexion.close()