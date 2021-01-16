from firebase_admin import credentials, initialize_app, storage

# Init firebase with your credentials
cred = credentials.Certificate("./e-menu-db-daf663b26d59.json")
initialize_app(cred, {'storageBucket': 'e-menu-db.appspot.com'})

# Đầu vào: link local
# Đầu ra: url public
def url_image_firebase(fileName):
    # Put your local file path
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("- Your file url", blob.public_url)
    return blob.public_url