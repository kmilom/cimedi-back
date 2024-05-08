from core.database import connectToDatabase

connection = connectToDatabase()
cursor = connection.cursor()

def getAllUsuarios():
    query = ("SELECT * FROM usuarios")
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def getUsuario(idUsuario: int):
    query = ("SELECT * FROM usuarios WHERE idUsuario = %s")
    cursor.execute(query, (idUsuario,))
    result = cursor.fetchone()
    return result

