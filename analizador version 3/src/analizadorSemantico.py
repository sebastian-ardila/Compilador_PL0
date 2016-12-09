txt = " "
cont = 0
def incremetarContador():
	global cont
	cont +=1
	return "%d" %cont

class Nodo():
	pass

class Null(Nodo):
	def __init__(self):
		self.type = 'void'

	def imprimir(self,ident):
		print ident + "nodo nulo"

	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id

class program(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id +"[label= "+self.name+"]"+"\n\t"

		txt += id +"->"+son1+"\n\t"

		return "digraph G {\n\t"+txt+"}"

class block(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4

	def imprimir(self,ident):

		#if str(type(self.son1)) == "<type 'tuple'>":
		if type(self.son1) == type(tuple()):
			#print "entro tupla"
			self.son1[0].imprimir(" "+ident)
		#elif str(type(self.son1)) == "<type 'instance'>":
		else:
			#print "entro instance"
			self.son1.imprimir(" "+ident)

		#if str(type(self.son2)) == "<type 'tuple'>":
		if type(self.son2) == type(tuple()):
			#print "entro tupla"
			self.son2[0].imprimir(" "+ident)
		#elif str(type(self.son2)) == "<type 'instance'>":
		else:
			#print "entro instance"
			self.son2.imprimir(" "+ident)

		#if str(type(self.son3)) == "<type 'tuple'>":
		if type(self.son3) == type(tuple()):
			#print "entro tupla"
			self.son3[0].imprimir(" "+ident)
		#elif str(type(self.son3)) == "<type 'instance'>":
		else:
			#print "entro instance"
			self.son3.imprimir(" "+ident)

		#if str(type(self.son4)) == "<type 'tuple'>":
		if type(self.son4) == type(tuple()):
			#print "entro tupla"
			self.son4[0].imprimir(" "+ident)
		#elif str(type(self.son4)) == "<type 'instance'>":
		else:
			#print "entro instance"
			self.son4.imprimir(" "+ident)


		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		if type(self.son1) == type(tuple()):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		if type(self.son2) == type(tuple()):
			son2 = self.son2[0].traducir()
		else:
			son2 = self.son2.traducir()

		if type(self.son3) == type(tuple()):
			son3 = self.son3[0].traducir()
		else:
			son3 = self.son3.traducir()

		if type(self.son3) == type(tuple()):
			son4 = self.son4[0].traducir()
		else:
			son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class constDecl(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		#self.son1.imprimir(" "+ident)

		self.son1.imprimir(" "+ident)

		# if type(self.son1) == type(tuple()):
		# 	self.son1[0].imprimir(" "+ident)
		# else:
		# 	self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		if type(self.son1) == type(tuple()):
			son1 = self.son1[0].traducir()
		else:
			son1 = self.son1.traducir()

		#son1 = self.son1.traducir()

		txt += id +"[label= "+self.name+"]"+"\n\t"
		txt += id +"->"+son1+"\n\t"

		return id

class constAssignmentList1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class constAssignmentList2(Nodo):
	def __init__(self,son1,son2,son3,son4,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3
		self.son4 = son4

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)
		self.son4.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()
		son4 = self.son4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"
		txt += id + " -> " + son4 + "\n\t"

		return id

class varDecl1(Nodo):
	def __init__(self,son1, name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class identList1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class identList2(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class procDecl1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):

		if type(self.son1) == type(tuple()):
			self.son1[0].imprimir(" "+ident)
		else:
			self.son1.imprimir(" "+ident)

		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class statement1(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class statement2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class statement3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class statement4(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2


	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		if type(self.son2) == type(tuple()):
			self.son2[0].imprimir(" "+ident)
		else:
			self.son2.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class statement5(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		if type(self.son2) == type(tuple()):
			self.son2[0].imprimir(" "+ident)
		else:
			self.son2.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class statementList1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class statementList2(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class condition1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class condition2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class relation1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class relation2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class relation3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class relation4(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class relation5(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class relation6(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class expression1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class expression2(Nodo):
	def __init__(self,son1,son2,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"

		return id

class expression3(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class addingOperator1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class addingOperator2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class term1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class term2(Nodo):
	def __init__(self,son1,son2,son3,name):
		self.name = name
		self.son1 = son1
		self.son2 = son2
		self.son3 = son3

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)
		self.son2.imprimir(" "+ident)
		self.son3.imprimir(" "+ident)

		print ident + "Nodo: "+self.name

	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()
		son2 = self.son2.traducir()
		son3 = self.son3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"
		txt += id + " -> " + son2 + "\n\t"
		txt += id + " -> " + son3 + "\n\t"

		return id

class multiplyingOperator1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class multiplyingOperator2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factor1(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factor2(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class factor3(Nodo):
	def __init__(self,son1,name):
		self.name = name
		self.son1 = son1

	def imprimir(self,ident):
		self.son1.imprimir(" "+ident)

		print ident + "Nodo: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()

		son1 = self.son1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + son1 + "\n\t"

		return id

class Id(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"ID: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id

class Assign(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):

		print ident+"Assign: "+self.name
			

	def traducir(self):
		global txt
		id = incremetarContador()
		
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class NE(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"NE: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class LT(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"LT: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class GT(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"GT: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class LTE(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"LTE: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class GTE(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"GTE: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Plus(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"Plus: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Minus(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"Minus: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Times(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"Times: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Divide(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"Divide: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Update(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"Update: "+self.name
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Number(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print ident+"Number: "+str(self.name)
			
	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id

# class empty(Nodo):
# 	def __init__(self,name):
# 		pass


