import sqlite3

clientes = [
    ('12345', 'Mario', 'Arjona', '23700981', '01148723458', 'marjona@gmail.com', 'ACTIVO'),
    ('98765','Alejandra','Sanchez','38407221','01184926574','asanchez@gmail.com','ACTIVO'),
    ('12345', 'Manuel', 'Belgrano', '124589638', '01132679472', 'mbelgrano@gmail.com','INACTIVO'),
    ('00751', 'Julieta', 'Mandalorian', '37889675', '01154399633','mandalirian1@gmail.com','ACTIVO'),
    ('00843', 'Soledad', 'Gorgelin', '33425786', '01166734324', 'gorge_sole@gmail.com','INACTIVO')
]

conexion = sqlite3.connect('./clientesBBDD.db')

cursor = conexion.cursor()
'''
cursor.execute('DROP TABLE clientes_2' )
conexion.commit()
conexion.close()

'''
'''
sentenciaSQL = 'CREATE TABLE clientes_2'
sentenciaSQL += '(id_cliente VARCHAR(30),'
sentenciaSQL += 'nombre VARCHAR(30),'
sentenciaSQL += 'apellido VARCHAR(30),'
sentenciaSQL += 'dni VARCHAR(30),'
sentenciaSQL += 'telefono VARCHAR(30),'
sentenciaSQL += 'email VARCHAR(40), '
sentenciaSQL += 'estado VARCHAR(30))'

cursor.execute(sentenciaSQL)
conexion.commit()
'''
'''
sentenciaSQL2 = "INSERT INTO clientes_2 VALUES (?,?,?,?,?,?,?)"
cursor.executemany(sentenciaSQL2, clientes)

conexion.commit()


'''
sentenciaSQL3 = "SELECT email FROM clientes_2 WHERE estado = 'ACTIVO'"
cursor.execute(sentenciaSQL3)
mails_activos = cursor.fetchall()

for mail in mails_activos:
    print(mail)

conexion.close()






