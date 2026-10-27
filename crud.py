from conexion import conectar_bd
import mysql.connector
    
    
def leer_registro(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM  paciente")
    resultados = cursor.fetchall()
    for paciente in resultados:
        print(paciente)
    cursor.close()
conexion =conectar_bd()
if conexion:
    leer_registro(conexion)
    #conexion.close
