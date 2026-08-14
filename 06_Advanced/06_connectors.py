# CONNECTORS
# Lección 19.1: https://youtu.be/OuJerKzV5T0?t=20876
# Lección 19.2: https://youtu.be/OuJerKzV5T0?t=21149

# Ejemplo de conexión desde Python a una base de datos local
# Se ejemplifica cómo evitar SQL INJECTION
from pathlib import Path

import mysql.connector


def print_user(user):

    config = {
        # Reutiliza las credenciales de [client] guardadas para el comando mysql.
        "option_files": str(Path.home() / ".my.cnf"),
        "option_groups": ["client"],
        "database": "hello_mysql",
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE name=%s;"
    print(query)
    cursor.execute(query, (user,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


print_user("Abraham")
# print_user("'; UPDATE users SET age = '15' WHERE user_id = 1; --")
