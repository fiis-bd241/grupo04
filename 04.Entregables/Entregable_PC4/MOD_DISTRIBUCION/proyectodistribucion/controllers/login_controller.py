from models.persona import Persona
from models.repartidor import Repartidor

def login(usuario, contraseña):
    # Autenticar en la tabla de personas
    persona = Persona.authenticate(usuario, contraseña)
    if persona:
        return persona.id_cargo

    # Autenticar en la tabla de repartidores
    repartidor_id = Repartidor.authenticate(usuario, contraseña)
    if repartidor_id:
        return repartidor_id  # Devuelve el ID del repartidor

    return None

