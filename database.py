from pymongo import MongoClient

def connect(database):
    try:
        client = MongoClient("mongodb+srv://root:2l4K6A2nl4tXDKmU@cluster0.e1tuqmv.mongodb.net/")
        db = client[database]
        print("Conexion a MongoDB establecida!")
        return db
    
    except Exception as e:
        print("Error de conexion a MongoDB: " + e)

def insertUser(collection, data):
    db = connect("test")
    db[collection].insert_one(data)
    print("Usuario registrado con exito")

def findUsers(collection):
    db = connect("test")
    return db[collection].find()

def testFindOne(collection, email):
    db = connect("test")
    result = db[collection].find_one({"email": email})
    return result