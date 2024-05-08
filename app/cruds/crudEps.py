from core.database import connectToDatabase

connection = connectToDatabase()
cursor = connection.cursor()

def getAllEps():
    query = ("SELECT * FROM eps")
    cursor.execute(query)
    results = cursor.fetchall()
    return results