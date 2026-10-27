from flask import Flask, render_template
from conexion import conectar_bd
import mysql.connector

app = Flask(__name__)

def leer_registros():
    conexion = conectar_bd()
    resultados =[]
    
    if conexion is None:
        print("error no se pudo establecer  la conexion a la base de datos")
        return resultados
    
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        resultados = cursor.fetchall()
        
    except mysql.connector.Error as error:
        print(f"error al leer los datos en sistema: {error}")
        
    finally:
        if cursor is not None:
            cursor.close()
        if conexion.is_connected():
            conexion.close()
            
    return resultados

@app.route('/')
def listar_pacientes():
    #1 obtener datos de la base de datos
    datos_pacientes = leer_registros()
    #2 rendelizar la plantilla html pasandole los datos
    return render_template(
        'pacientes.html',
        pacientes=datos_pacientes,
        titulo='Listas de Pacientes'
    )

if __name__=='__main__':
    #Asegurate de que tu servidor mysql este corriendo
    app.run(debug=True)
