loop = True
while(loop == True):
	a = input("Vamos verificar caracteristicas, digite algo: ")
	print("Em maiusculas: {}".format(a.isupper()))
	print("Em minusculas: {}".format(a.islower()))
	print("É numerico: {}".format(a.isnumeric()))
	print("É alfabetico: {}".format(a.isalpha()))
	print("É alfanúmerico: {}".format(a.isalnum()))
	print("É capitalizado: {}".format(a.istitle()))
