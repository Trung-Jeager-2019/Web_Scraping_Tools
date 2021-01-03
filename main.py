from selenium import webdriver
from product import *
import pyodbc
import requests


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

server = 'e-menu.database.windows.net'
database = 'e-menu'
username = 'admin_db'
password = 'TrungHieu#'   
driver = '{ODBC Driver 17 for SQL Server}'

connect = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

# ------------------------------------------------------------------------------------------------------
PATH = "D:\Downloads\Software Files\chromedriver_win32\chromedriver.exe"

code_menu_item = ['ca-phe-viet-nam', 'ca-phe-may', 'cold-brew', 'tra-trai-cay', 'tra-sua-macchiato',
    'ca-phe-da-xay', 'thuc-uong-trai-cay', 'matcha-socola', 'banh-snack', 'ca-phe-goi', 'merchandise']

for menu_item in code_menu_item:

    driver = webdriver.Chrome(PATH)

    driver.get('https://www.thecoffeehouse.com/collections/menu')

    id_menu_item = driver.find_element_by_id(str(menu_item))

    # Tên danh mục
    name_item_menu = id_menu_item.find_element_by_class_name("line_after_heading").text
    # Mã danh mục
    code_item_menu = menu_item
    print(code_item_menu + " - " + name_item_menu)

    cursor = connect.cursor()

    cursor.execute(""" INSERT INTO Menu_Dien_Tu_App_category (category_code, category_name) 
    VALUES (?,?)""", code_item_menu, name_item_menu) 

    connect.commit()

    links = id_menu_item.find_elements_by_css_selector("a")

    list_unique_product = Check_Link_Product(links)

    # print([product_link for product_link in list_unique_product])

    for product_link in list_unique_product:
        
        print(product_link)
        data = Get_Data_Product(product_link, driver)
        # Tên sản phẩm
        print(data.get('product_title'))
        # Mô tả sản phẩm
        print(data.get('product_description'))
        # Giá cả sản phẩm
        print(data.get('product_price'))
        # Hình ảnh sản phẩm
        print(data.get('product_image'))

        name_image = product_link.split("/", 4)[-1] + ".jpg"

        # r = requests.get(data.get('product_image'))
        # with open("D:/Documents/Study_in_University/Four_year/Database_management_system/Project/He_thong_Menu_Dien_Tu/media/upload/" + name_image, "wb") as f:
        #     f.write(r.content)

        link_image = "upload/" + name_image
        
        price = data.get('product_price').split(",", 1)[0] + "000"
        
        # cursor = connect.cursor()

        # cursor.execute("""INSERT INTO Menu_Dien_Tu_App_menuitem (name, price, image, active, user_id, describe, category) 
        # VALUES (?,?,?,?,?,?,?)""", data.get('product_title'), price, link_image, True, 2, data.get('product_description'), code_item_menu) 

        # # cursor.execute(""" UPDATE {}  SET {} = '{}' where {} = '{}' """.format(
        # #     "Menu_Dien_Tu_App_menuitem", "category", code_item_menu, "image", link_image))

        # connect.commit()

    driver.close()

driver.quit()