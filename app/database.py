import sqlite3


def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)

    result = cursor.fetchall()
    connection.close()

    return result

def get_user_by_id(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE id = ?"

    cursor.execute(query, (user_id,))

    result = cursor.fetchall()
    connection.close()

    return result

def get_user_by_email_insecure(email):
    """
    EJEMPLO INSEGURO PARA PRUEBAS DE SECUREFLOW AI.
    No utilizar en producción.
    """
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE email = '" + email + "'"
    cursor.execute(query)

    result = cursor.fetchall()
    connection.close()

    return result