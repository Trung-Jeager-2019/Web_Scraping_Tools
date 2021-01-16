# import mysql.connector
# import sshtunnel
# import pymysql.cursors

# sshtunnel.SSH_TIMEOUT = 5.0
# sshtunnel.TUNNEL_TIMEOUT = 5.0

# with sshtunnel.SSHTunnelForwarder(
#     ('ssh.pythonanywhere.com', 22),
#     ssh_username='SherwinTrung', ssh_password='Trung0989481984#',
#     remote_bind_address=('SherwinTrung.mysql.pythonanywhere-services.com', 3306)
# ) as tunnel:
#     # connection = mysql.connector.connect(
#     #     user='SherwinTrung', password='Trung14121999#',
#     #     host='127.0.0.1', port=tunnel.local_bind_port,
#     #     database='SherwinTrung$restaurant_db',
#     # )
#     connection = pymysql.connect(host='127.0.0.1',
#                              user='SherwinTrung',
#                              password='Trung14121999#',                             
#                              db='SherwinTrung$restaurant_db',
#                              port=tunnel.local_bind_port,
#                              cursorclass=pymysql.cursors.DictCursor)
#     # Do stuff
#     connection.close()

# ------------------------------------------------------------------------------------------------------
# connect = pyodbc.connect('Driver={sql server};'
#                             'Server=DESKTOP-AJ7H4HH\MSSQLSERVER2019;'
#                             'Database=restaurant_db;'
#                             'Trusted_Connection=yes;')
# connect = mysql.connector.connect(
#   host="SherwinTrung.mysql.pythonanywhere-services.com",
#   database="SherwinTrung$restaurant_db",
#   user="SherwinTrung",
#   password="Trung14121999#"
# )
# ------------------------------------------------------------------------------------------------------

# import pyodbc

# server = 'e-menu.database.windows.net'
# database = 'e-menu'
# username = 'admin_db'
# password = 'TrungHieu#'   
# driver = '{ODBC Driver 17 for SQL Server}'

# with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT category_code, category_name FROM Menu_Dien_Tu_App_category")
#         row = cursor.fetchone()
#         while row:
#             print (str(row[0]) + " " + str(row[1]))
#             row = cursor.fetchone()
# ------------------------------------------------------------------------------------------------------

# server = 'e-menu.database.windows.net'
# database = 'e-menu'
# username = 'admin_db'
# password = 'TrungHieu#'   
# driver = '{ODBC Driver 17 for SQL Server}'

# connect = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

# cursor = connect.cursor()

# cursor.execute("""INSERT INTO Menu_Dien_Tu_App_menuitem (name, price, image, active, user_id, describe, category) 
# VALUES (?,?,?,?,?,?,?)""", data.get('product_title'), price, link_image, True, 2, data.get('product_description'), code_item_menu) 

# cursor.execute(""" UPDATE {}  SET {} = '{}' where {} = '{}' """.format(
#     "Menu_Dien_Tu_App_menuitem", "category", code_item_menu, "image", link_image))

# connect.commit()

# cursor = connect.cursor()

# cursor.execute(""" INSERT INTO Menu_Dien_Tu_App_category (category_code, category_name) 
# VALUES (?,?)""", code_item_menu, name_item_menu) 

# connect.commit()

# import pathlib

# py = pathlib.Path().glob("upload/*.jpg")
# for file in py:
#     print(file)