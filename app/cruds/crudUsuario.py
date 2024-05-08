from typing import List, Optional
import mysql.connector
from core.database import connectToDatabase
from models.userModel import Usuario


# Función para obtener todos los usuarios de la base de datos
def getAllUsuarios() -> List[Usuario]:
    # Establecer conexión a la base de datos
    connection = connectToDatabase()

    # Inicializar una lista para almacenar los usuarios
    usuarios = []

    try:
        # Crear cursor
        cursor = connection.cursor(dictionary = True)

        # Ejecutar consulta para obtener todos los usuarios
        query = "SELECT idUsuario, User, Password, idRol FROM Usuarios"
        cursor.execute(query)

        # Obtener resultados y convertirlos a objetos Usuario
        for row in cursor.fetchall():
            usuario = Usuario(**row)
            usuarios.append(usuario)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener usuarios: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            
    return usuarios

#Función para obtener un usuario por su id
def getUsuarioById(idUsuario: int) -> Optional[Usuario]:
    connection = connectToDatabase()
    usuario = None

    try:
        cursor = connection.cursor(dictionary = True)
        query = "SELECT idUsuario, User, Password, idRol FROM Usuarios WHERE idUsuario = %s"
        cursor.execute(query, (idUsuario,))
        row = cursor.fetchone()
        if row:
            usuario = Usuario(**row)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener usuarios: {e}")
    return usuario

#Función para crear un usuario
def crearUsuario(usuario: Usuario):
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()
        query = "INSERT INTO Usuarios (idUsuario, User, Password, idRol) VALUES (%s, %s, %s, %s)"
        cursor.execute(query,(usuario.idUsuario, usuario.User, usuario.Password, usuario.idRol))
        #Para proteger la integridad de los datos
        connection.commit()
        return True
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return False
    finally:
        connection.close()
