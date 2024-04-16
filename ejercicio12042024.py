class Persona:
    def __init__(self, nombre, edad, direccion, telefono, email, ocupacion, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.ocupacion = ocupacion
        self.nacionalidad = nacionalidad

    def __str__(self):
        return(
            f"\nNombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"Dirección: {self.direccion}\n"
            f"Teléfono: {self.telefono}\n"
            f"Email: {self.email}\n"
            f"Ocupación: {self.ocupacion}\n"
            f"Nacionalidad: {self.nacionalidad}"
        )

if __name__ == "__main__":
    p1 = Persona("Jorge", 26, "Ixtapaluca, Estado de Mexico", "123456789", "jorge26@ipn.mx", "Ingeniero", "Mexicana")
    print(p1)
