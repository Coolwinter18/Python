import psycopg2 as db

conexion = db.connect(user="postgres",
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')


cursor = conexion.cursor()
query = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
valores = (
    ('Marcos','Cantu','mcantu@mail.com'),
    ('Angel','Quintana','aquintana@mail.com'),
    ('Maria','Gonzalez','mgonzalez@mail.com'),
)
cursor.executemany(query,valores)
conexion.commit()
reg_insertados = cursor.rowcount
print(f'Registros insertados: {reg_insertados}')

cursor.close()
conexion.close()