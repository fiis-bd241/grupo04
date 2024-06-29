# controllers/login_controller.py

def login(usuario, contraseña, role=None):
    # Tu lógica actual de autenticación
    # Puedes usar el argumento 'role' para manejar diferentes tipos de usuarios
    # Por ejemplo, aquí podrías verificar el rol y devolverlo o manejarlo según sea necesario
    # Ejemplo básico:
    if role == "GDT":
        # Verificar autenticación para Gestor de Distribución
        # Devolver el rol o ID adecuado
        return "GDT"
    elif role == "CLI":
        # Verificar autenticación para Cliente
        # Devolver el rol o ID adecuado
        return "CLI"
    elif role == "RPT":
        # Verificar autenticación para Repartidor
        # Devolver el rol o ID adecuado
        return "RPT"
    else:
        # Lógica para manejar otros casos o retornar None o algún indicador de error
        return None

