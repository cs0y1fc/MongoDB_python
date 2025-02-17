from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb+srv://root:2l4K6A2nl4tXDKmU@cluster0.e1tuqmv.mongodb.net/")
    db = client["test"]
    return db

def insertUser(db, collection, data):
    db[collection].insert_one(data)
    print("Usuario registrado con exito")

def findUsers(db, collection):
    return db[collection].find()

def find_by_email(db, collection, email):
    return db[collection].find_one({"email": email})

def insertPurchase(db, collection, email, data):
    result = db[collection].update_one(
        {"email": email},
        {"$push": {"compras": data}}
    )

    result = dict(result.raw_result)

    if result["updatedExisting"]: 
        print("Compra realizada")
    else:
        print("Usuario no registrado en nuestra app")   

def delete_by_email(db, collection, email):
    return db[collection].delete_one({"email": email})