import psycopg2 as db

conexion = db.connect(user="postgres",
                 password='1234',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')


cursor = conexion.cursor()
query = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
valores = ('Carlos','Lara','clara@mail.com')
cursor.execute(query,valores)
conexion.commit()
reg_insertados = cursor.rowcount
print(f'Registros insertados: {reg_insertados}')

cursor.close()
conexion.close()