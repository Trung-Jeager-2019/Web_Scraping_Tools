def Menu_Item(driver):

    code_menu_item = ['ca-phe-viet-nam', 'ca-phe-may', 'cold-brew', 'tra-trai-cay', 'tra-sua-macchiato',
    'ca-phe-da-xay', 'thuc-uong-trai-cay', 'matcha-socola', 'banh-snack', 'ca-phe-goi', 'merchandise']
    
    name_menu_item = []
    
    for menu_item in code_menu_item:

        id_menu_item = driver.find_element_by_id(menu_item)

        name_menu_item.append(id_menu_item.find_element_by_class_name("line_after_heading").text)

    # print(dict(zip(code_menu_item, name_menu_item)))

def Check_Link_Product(list_product_links):

    list_unique_product = []

    for link in list_product_links:

        str_link = link.get_attribute('href')

        check_first = str_link.split("/", 2)[2].split(".", 1)[0]

        if check_first != "order":

            if str_link not in list_unique_product:

                list_unique_product.append(str_link)

    print(len(list_unique_product))

    return [link for link in list_unique_product]


def Get_Data_Product(link, driver):
    
    driver.get(link)

    dict_unique_product = {}
    # Lấy link ảnh
    # links = menu_item.find_elements_by_css_selector("img")

    # for link in links:
    #     print(link.get_attribute('src'))
    dict_unique_product['product_title'] = driver.find_element_by_class_name("info_product_title").text

    try:
        
        dict_unique_product['product_description'] = driver.find_element_by_class_name("info_product_short_des").text
    
    except Exception as Ex:
        
        dict_unique_product['product_description'] = driver.find_element_by_class_name("product_description").text

    dict_unique_product['product_price'] = driver.find_element_by_class_name("product_price").text
    
    dict_unique_product['product_image'] = driver.find_element_by_class_name("product_featured_image").get_attribute('src')

    return dict_unique_product