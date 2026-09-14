class Persona :
    def __init__(self, documento, nombre, apellido , edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido= apellido
        self.edad = edad
        
    def __str__(self):
        return f"Documento: {self.documento}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"
    
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'
    
    def es_mayor_edad(self):
        return self.edad >= 18
    
    