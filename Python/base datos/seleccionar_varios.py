import psycopg2 as db

conexion = db.connect(user="postgres",
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

entrada = input("Proporciona las pk a buscar (separado por comas): ")
cursor = conexion.cursor()
query = 'SELECT * FROM persona WHERE id_persona IN %s'
tupla = tuple(entrada.split(','))
#print(tupla)
llaves_primarias = (tupla,)
cursor.execute(query,llaves_primarias)
resultado_query = cursor.fetchall()
for registro in resultado_query:
    print(registro)

cursor.close()
conexion.close()