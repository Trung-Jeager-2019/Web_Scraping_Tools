import pyrebase

pyrebaseConfig = {
    "databaseURL" : "https://e-menu-db-default-rtdb.firebaseio.com/",
    "apiKey": "AIzaSyDfb1S19IRtFwUnE5yKKUDwi13giPdGrl0",
    "authDomain": "e-menu-db.firebaseapp.com",
    "projectId": "e-menu-db",
    "storageBucket": "e-menu-db.appspot.com",
    "messagingSenderId": "482398126259",
    "appId": "1:482398126259:web:d5c7146ed44e99a1bbf0c6",
    "measurementId": "G-HDPJM7LRBY"
}

firebase = pyrebase.initialize_app(pyrebaseConfig)

db = firebase.database()

# Push Data
data = {"name":"Trung", "age":20, "address":"QuyNhon, DinhBinh"}

# db.push(data)

db.child("trung").set(data)