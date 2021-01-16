from selenium import webdriver
import requests
from unidecode import unidecode

from product import Check_Link_Product, Get_Data_Product
from upload_image import url_image_firebase
from api_post import response_data

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

    links = id_menu_item.find_elements_by_css_selector("a")

    list_unique_product = Check_Link_Product(links)

    # Sản phẩm thuộc theo danh mục
    for product_link in list_unique_product:
        
        print(product_link)
        data = Get_Data_Product(product_link, driver)
        # Tên sản phẩm
        print(data.get('product_title'))
        # Giá cả sản phẩm
        print(data.get('product_price'))
        # Hình ảnh sản phẩm
        print(data.get('product_image'))
        # Mô tả sản phẩm
        print(data.get('product_description'))

        category_name = data.get('product_title')
        category_list = category_name.split()
        sub_str = ''
        for item in category_list:
            if item.isalnum():
                lower_item = unidecode(item.lower()) + "-"
                print(lower_item)
                sub_str += lower_item
        category_code = sub_str.rsplit('-', 1)[0]
        print(category_code)
        name_image = category_code + ".jpg"

        # Lưu ảnh về Local
        r = requests.get(data.get('product_image'))
        with open("./upload/" + name_image, "wb") as f:
            f.write(r.content)

        # Link ảnh ở local
        link_image_local = "upload/" + name_image
        
        # Tên sản phẩm
        name = data.get('product_title')

        # Link ảnh ở public - Đẩy ảnh lên Firebase
        link_image_public = url_image_firebase(link_image_local)

        # Giá cả sản phẩm
        price = data.get('product_price').split(",", 1)[0] + "000"
        
        # Mô tả sản phẩm
        decribe = data.get('product_description')
        
        url = "http://127.0.0.1:8000/"
        payload = {
            'category': name_item_menu,
            'name': name,
            'price': price,
            'image': link_image_public,
            'decribe': decribe
        }
        files = []
        headers = {}
        # Đẩy dữ liệu về api - Post
        response_data(url, payload, files, headers)

    driver.close()

    driver.quit()