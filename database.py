import pyodbc

def run_query(intent):
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=your_server_name;'  # Replace with your server name
        r'DATABASE=your_database_name;'  # Replace with your database name
        r'Trusted_Connection=yes;'  # Use this for Windows authentication
        # r'UID=your_username;'  # Uncomment these lines and add your username/password for SQL Server authentication
        # r'PWD=your_password;'
    )
    
    # Connect to the database
    conn = pyodbc.connect(conn_str)

    # Depending on the intent, run a different SQL query
    if intent == 'average_mission_time':
        query = 'Your SQL query here'  # Replace with your SQL query
    else:
        return 'Unknown query'

    # Run the query and fetch the results
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    return rows
