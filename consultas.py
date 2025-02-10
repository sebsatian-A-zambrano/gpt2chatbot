import sqlite3

def ejecutar_consulta(consulta, params=None):
    # Conectar a la base de datos
    conn = sqlite3.connect('ventas_placas_video.db')
    cursor = conn.cursor()

    try:
        # Ejecutar la consulta con o sin parámetros
        if params:
            cursor.execute(consulta, params)
        else:
            cursor.execute(consulta)
        
        # Obtener todos los resultados
        resultados = cursor.fetchall()
        
        # Devolver los resultados
        return resultados
    except sqlite3.Error as e:
        # En caso de error, devolver el mensaje de error
        return f"Error al ejecutar la consulta: {e}"
    finally:
        # Cerrar la conexión a la base de datos
        conn.close()

def mostrar_resultados(respuesta):
    # Mostrar los resultados de la consulta
    if isinstance(respuesta, list):
        if respuesta:  # Si hay resultados
            for row in respuesta:
                print("Respuesta:", row[0] if len(row) == 1 else row)
        else:
            print("No se encontraron resultados.")
    else:
        print("Error:", respuesta)