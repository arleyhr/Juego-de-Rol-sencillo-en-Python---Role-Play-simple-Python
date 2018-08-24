import random,os,time

def limpiar():
	os.system("cls")

class Jugador(object):
	def __init__(self,nombre):
		self.nombre = nombre
		self.hp_max = random.randrange(60,71)
		self.mp_max = random.randrange(30,41)
		self.fuerza = random.randrange(3,7)
		self.inteligencia = random.randrange(2,5)
		self.hp = self.hp_max
		self.mp = self.mp_max
		self.habilidades = [BolaDeFuego(),GolpeLetal(),Golpear()]
		 
	def __str__(self):
		return "Jugador: "+str(self.nombre)+" HP: "+str(self.hp)+"/"+str(self.hp_max)+"  MP: "+str(self.mp)+"/"+str(self.mp_max)
	
	def stats(self):
		print(self.nombre)
		print("HP:",self.hp,"/",self.hp_max)
		print("HP:",self.mp,"/",self.mp_max)
		print("Fuerza:",self.fuerza)
		print("Inteligencia:",self.inteligencia)
		
	def eleccion(self):
		print("\nElige una habilidad:\n")
		print("0 - Bola de fuego (10 MP)")
		print("1 - Golpe letal (5 MP)")
		print("2 - Golpear (0 MP)")
		x = input(">")
		return int(x)

class AI(object):
	def __init__(self):
		self.nombre = "AI"
		self.hp_max = random.randrange(60,71)
		self.mp_max = random.randrange(30,41)
		self.fuerza = random.randrange(3,7)
		self.inteligencia = random.randrange(2,5)
		self.hp = self.hp_max
		self.mp = self.mp_max
		self.habilidades = [BolaDeFuego(),GolpeLetal(),Golpear()]
		 
	def __str__(self):
		return "Jugador: "+self.nombre+" HP: "+str(self.hp)+"/"+str(self.hp_max)+"  MP: "+str(self.mp)+"/"+str(self.mp_max)
	
	def stats(self):
		print(self.nombre)
		print("HP:",self.hp,"/",self.hp_max)
		print("HP:",self.mp,"/",self.mp_max)
		print("Fuerza:",self.fuerza)
		print("Inteligencia:",self.inteligencia)
	
	def eleccion(self):
		x = random.randrange(0,3)
		return x

class BolaDeFuego(object):
	def __init__(self):
		self.danio = 0
		self.nombre = "Bola de fuego"
	
	def devolverAtaque(self,origen):
		if origen.mp<10:
			return 0
		else:
			self.danio = random.randrange(21,26)+origen.inteligencia
			origen.mp += -10
		return self.danio
	
		
class GolpeLetal(object):
	def __init__(self):
		self.danio = 0
		self.nombre = "Golpe letal"
		
	def devolverAtaque(self,origen):
		if origen.mp<5:
			return 0
		else:
			self.danio = random.randrange(12,16)+origen.fuerza
			origen.mp += -5
			return self.danio

class Golpear(object):
	def __init__(self):
		self.danio = 0
		self.nombre = "Golpear"
		
	def devolverAtaque(self,origen):
		self.danio = origen.inteligencia+origen.fuerza
		return self.danio
		
	def restar_costos(self,origen):
		pass

def main():
	print(" WELCOME!!!\n --------------------------")
	nombre = input(" Escribe tu nombre: ")
	j1 = Jugador(nombre)
	j2 = AI()
	print(" --------------------------")
	print("Jugador 1:")
	print(j1.stats())
	print(" --------------------------")
	print(" --------------------------")
	print("Jugador 2:")
	print(j2.stats())
	print(" --------------------------")
	time.sleep(5)
	limpiar()
	while j1.hp>0 and j2.hp>0:
		limpiar()
		print("---------------")
		print(j1)
		print("---------------")
		print(j2)
		print("---------------")
		
		print("\nTURNO DE",j1.nombre)
		elec1 = j1.eleccion()
		j2.hp -=  j1.habilidades[elec1].devolverAtaque(j1)
		print("Haz usado ",j1.habilidades[elec1].nombre)
		print("Atacando...")
		time.sleep(1)
		print("Danio",j1.habilidades[elec1].devolverAtaque(j1))
		time.sleep(0.5)
		if j1.hp<=0 and j2.hp<=0:
			break
		
		print("\nTurno de",j2.nombre)
		elec2 = j2.eleccion()
		j1.hp -=  j2.habilidades[elec2].devolverAtaque(j2) 
		print(j2.nombre,"a usado ",j2.habilidades[elec2].nombre)
		print("Atacando...")
		time.sleep(1)
		print("Danio",j2.habilidades[elec2].devolverAtaque(j2))
		time.sleep(2)
		if j1.hp<=0 or j2.hp<=0:
			break
	if j1.hp>0:
		print("Gano",j1.nombre)
	else:
		print("Gano",j2.nombre)
main()
