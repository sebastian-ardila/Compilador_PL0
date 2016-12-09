import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
from analizadorSemantico import *

precedence = (
	('right','ID','CALL','BEGIN','IF','WHILE'),
	('right','PROCEDURE'),
	('right','VAR'),
	('right', 'ASSIGN'),
	('right','UPDATE'),
	('left','NE'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','ODD'),
	('left','LPARENT','RPARENT'),
	)

def p_program(p):
	'''program : block'''
	#print "program"
	p[0] = program(p[1],"program")

def p_block(p):
	'''block : constDecl varDecl procDecl statement'''
	p[0] = block(p[1],p[2],p[3],p[4],"block")
	#print "block"

def p_constDecl(p):
	'''constDecl : CONST constAssignmentList SEMMICOLOM'''
	p[0] = constDecl(p[2],"constDecl")
	#print "constDecl"

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	p[0] = Null()
	#print "nulo"

def p_constAssignmentList1(p):
	'''constAssignmentList : ID ASSIGN NUMBER'''
	p[0] = constAssignmentList1(Id(p[1]),Assign(p[2]),Number(p[3]),"constAssignmentList1")
	#print "constAssignmentList 1"

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBER'''
	p[0] = constAssignmentList2(p[1],Id(p[3]),Assign(p[4]),Number(p[5]),"constAssignmentList2")
	#print "constAssignmentList 2"

def p_varDecl1(p):
	'''varDecl : VAR identList SEMMICOLOM'''
	p[0] = varDecl1(p[2],"VarDecl1")
	#print "varDecl 1"

def p_varDeclEmpty(p):
	'''varDecl : empty'''
	p[0] = Null()
	#print "nulo"

def p_identList1(p):
	'''identList : ID'''
	p[0] = identList1(Id(p[1]),"identList1")
	#print "identList 1"

def p_identList2(p):
	'''identList : identList COMMA ID'''
	p[0] = identList2(p[1],Id(p[3]),"identList2")
	#print "identList 2"

def p_procDecl1(p):
	'''procDecl : procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOM'''
	p[0] = procDecl1(p[1],Id(p[3]),p[5],"procDecl1")
	#print "procDecl 1"

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	p[0] = Null()
	#print "nulo"

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	p[0] = statement1(Id(p[1]),Update(p[2]),p[3],"statement1")
	#print "statement 1"

def p_statement2(p):
	'''statement : CALL ID'''
	p[0] = statement2(Id(p[2]),"statement2")
	#print "statement 2"

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	p[0] = statement3(p[2],"statement3")
	#print "statement 3"

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	p[0] = statement4(p[2],p[4],"statement4")
	#print "statement 4"

def p_statement5(p):
	'''statement : WHILE condition DO statement'''
	p[0] = statement5(p[2],p[4],"statement5")
	#print "statement 5"

def p_statementEmpty(p):
	'''statement : empty'''
	p[0] = Null()
	#print "nulo"

def p_statementList1(p):
	'''statementList : statement'''
	p[0] = statementList1(p[1],"statementList1")
	#print "statementList 1"

def p_statementList2(p):
	'''statementList : statementList SEMMICOLOM statement'''
	p[0] = statementList2(p[1],p[3],"statementList2")
	#print "statementList 2"

def p_condition1(p):
	'''condition : ODD expression'''
	p[0] = condition1(p[2],"condition1")
	#print "condition 1"

def p_condition2(p):
	'''condition : expression relation expression'''
	p[0] = condition2(p[1],p[2],p[3],"condition2")
	#print "condition 2"

def p_relation1(p):
	'''relation : ASSIGN'''
	p[0] = relation1(Assign(p[1]),"relation1")
	#print "relation 1"

def p_relation2(p):
	'''relation : NE'''
	p[0] = relation2(NE(p[1]),"relation2")
	#print "relation 2"

def p_relation3(p):
	'''relation : LT'''
	p[0] = relation3(LT(p[1]),"relation3")
	#print "relation 3"

def p_relation4(p):
	'''relation : GT'''
	p[0] = relation4(GT(p[1]),"relation4")
	#print "relation 4"

def p_relation5(p):
	'''relation : LTE'''
	p[0] = relation5(LTE(p[1]),"relation5")
	#print "relation 5"

def p_relation6(p):
	'''relation : GTE'''
	p[0] = relation6(GTE(p[1]),"relation6")
	#print "relation 6"

def p_expression1(p):
	'''expression : term'''
	p[0] = expression1(p[1],"expression1")
	#print "expresion 1"

def p_expression2(p):
	'''expression : addingOperator term'''
	p[0] = expression2(p[1],p[2],"expression2")
	#print "expresion 2"

def p_expression3(p):
	'''expression : expression addingOperator term'''
	p[0] = expression3(p[1],p[2],p[3],"expression3")
	#print "expresion 3"

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	p[0] = addingOperator1(Plus(p[1]),"addingOperator")
	#print "addingOperator 1"

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	p[0] = addingOperator2(Minus(p[1]),"subtractionOperator")
	#print "addingOperator 1"

def p_term1(p):
	'''term : factor'''
	p[0] = term1(p[1],"term1")
	#print "term 1"

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	p[0] = term2(p[1],p[2],p[3],"term2")
	#print "term 1"

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	p[0] = multiplyingOperator1(Times(p[1]),"multiplyingOperator")
	#print "multiplyingOperator 1"

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	p[0] = multiplyingOperator2(Divide(p[1]),"divisiongOperator")
	#print "multiplyingOperator 2"

def p_factor1(p):
	'''factor : ID'''
	p[0] = factor1(Id(p[1]),"factor1")
	#print "factor 1"

def p_factor2(p):
	'''factor : NUMBER'''
	p[0] = factor2(Number(p[1]),"factor2")
	#print "factor 1"

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	p[0] = factor3(p[2],"factor3")
	#print "factor 1"

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print "Error de sintaxis ", p
	#print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has escogido \"%s\"" %files[int(numArchivo)-1]

	return files[int(numArchivo)-1]

def traducir(result):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print "El programa traducido se guardo en \"graphviztrhee.vz\""

directorio = '/Users/sebas/Documents/Compiladores/pl0/analizador version 2/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena,debug=1)

#result.imprimir(" ")
#print result.traducir()
traducir(result)



#print result











