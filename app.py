import database, utils

def app():

    db = database.connect()

    while True:
        # menu
        print("------ Users --------")
        print("1: Añadir un usuario")
        print("2: Ver usuarios")
        print("3: Buscar usuario por email")
        print("----- Purchases -----")
        print("4: Añadir un compra (embedded)")
        print("5: Añadir un compra (referenced)")
        print("Escribe 'exit' para salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")

            email = input("Email: ")
            while not utils.validar_email(email):
                email = input("Introduce un email correcto: ")
        
            password = input("Contraseña: ")
            # validar si el email ya esta registrado en la app
            if database.find_by_email(db, "users", email):
                print("Email ya registrado en la app")
            else:
                # creamos una variable tipo dict(diccionario) igual que un JSON
                data = {
                    "nombre": nombre,
                    "email": email,
                    "password": utils.encriptar(password)
                }
                database.insertUser(db, "users", data)

        if opcion == "2":
            usersObj = database.findUsers(db, "users")
            for user in usersObj: 
                print(user)
        
        if opcion == "3":
            email = input("Email: ")
            user = database.find_by_email(db, "users", email)
            if user:
                print(user)
            else:
                print("Usuario no encontrado")

        if opcion == "exit":
            print("Bye")
            exit()

app()