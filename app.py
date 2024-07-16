import database, bcrypt

def verificarEmail(email):
        res = database.testFindOne("users", email)
        if res: 
             print("email ya creado")
        else: 
             print("Email no creado")

while True:
    # menu
    print("1: Añadir un usuario")
    print("2: Ver usuarios")
    print("3: Buscar usuario por email")
    print("Escribe 'exit' para salir")
    

    opcion = input("Seleccione una Opcion: ")

    


    if opcion == "1":
        nombre = input("Nombre: ")
        email = input("Email: ")
        password = input("Password: ")
        passhashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        verificarEmail(email)
# Creamos una variable tipo dict(diccionario) igual que un JSON
        data = {
            "nombre": nombre,
            "email": email,
            "password": passhashed
        }

        database.insertUser("users", data)

    if opcion =="2":
        usersObj = database.findUsers("users")
        for user in usersObj:
            print(user)
      

    if opcion == "exit":
        print("Bye")
        exit()
