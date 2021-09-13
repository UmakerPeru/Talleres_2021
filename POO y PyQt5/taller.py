
class Humano:
	def __init__(self,nombre,edad):#metodos magicos
		self.nombre = nombre
		self.edad = edad
	def hablar(self): #metodos de instancia
		print("Hola soy un objeto")

class Estudiante(Humano):

	def __init__(self,nombre,edad,peso):
		super().__init__(nombre,edad)
		self.peso = peso
	def carrera(self):
		print("soy" ,self.nombre,"Estudio Ingenieria")
juan = m.Humano("juan",27) #instanciado la clase
juan.hablar() #objeto.metodo
print(juan.edad) #objeto.atributo

carmen = m.Estudiante("carmen",19,60)
carmen.hablar()
carmen.carrera()
