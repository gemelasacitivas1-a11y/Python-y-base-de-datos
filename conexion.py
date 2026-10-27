import mysql.connector
def conectar_bd():
    try: 
        conexion = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "",
            database= "clinica_andrea",
            port= 3306
            )
    
        print("conexion con la base exitosa")
        return conexion
    except mysql.connector.Error as error:
        print(f"error al conectarse")
        return None
    except Exception as error :
        print(f"error inesperado")
        return None 

conectar = conectar_bd()
    
