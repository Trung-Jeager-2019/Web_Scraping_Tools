# import mysql.connector
# import sshtunnel

# sshtunnel.SSH_TIMEOUT = 5.0
# sshtunnel.TUNNEL_TIMEOUT = 5.0

# with sshtunnel.SSHTunnelForwarder(
#     ('ssh.pythonanywhere.com', 22),
#     ssh_username='SherwinTrung', ssh_password='Trung0989481984#',
#     remote_bind_address=('SherwinTrung.mysql.pythonanywhere-services.com', 3306)
# ) as tunnel:
#     connection = mysql.connector.connect(
#         user='SherwinTrung', password='Trung14121999#',
#         host='127.0.0.1', port=tunnel.local_bind_port,
#         database='SherwinTrung$restaurant_db',
#     )
#     # Do stuff
#     connection.close()

# ------------------------------------------------------------------------------------------------------

import pyodbc

server = 'e-menu.database.windows.net'
database = 'e-menu'
username = 'admin_db'
password = 'TrungHieu#'   
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT category_code, category_name FROM Menu_Dien_Tu_App_category")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()