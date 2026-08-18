import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NewPass123!",
        database="project_lifeline",
        port=3306
    )
    print("✅ Connection successful!")
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    print(f"Current database: {result[0]}")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")