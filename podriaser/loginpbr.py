usuarios = {}

def registrar_usuario():
    usuario = input("Ingresa un nombre de usuario: ")
    if usuario in usuarios:
        print("Este usuario ya existe. Por favor, elige otro.")
    else:
        contraseña = input("Ingresa una contraseña: ")
        usuarios[usuario] = contraseña
        print("Usuario registrado con éxito.")

def iniciar_sesion():
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")