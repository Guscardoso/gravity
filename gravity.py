#CALCULADORA GRAVITACIONAL
print("""CALCULADORA GRAVITACIONAL:
          1-gravidade de um planeta
          2-força gravitacional entre
          dois corpos
          3-velocidade de um satélite  
          obs: use unidades em kg e m""")
n = input ("Escolha:")
if n==1:
   m = int (input  ("Massa do planeta:"))
   r = int (input  ("Raio do planeta:"))
   k = (6.7/(10**11))
   g =( (k*m)/(r**2))
   print("A aceleração é", g,"m/s^2")
if n==2:
	m1 = int (input  ("Massa 1:"))
	m2 = int (input  ("Massa 2:"))
	r = int (input  ("Distância entre as duas massas:"))
	k = (6.7/(10**11))
	f = ((k*m1*m2)/r**2)
	print("A força é de ",f,"N")
if n==3:
   print ("velocidade de um satélite na órbita terrestre")
   h = int ( input  ("Altura do do satélite :"))
   r = ((6.37)*(10**6))
   m = ( 5.98*(10**24))
   k = (6.7/(10**11))
   v = ((k*m)/((r+h)**2))**1/2
   print("A velocidade é",v,"m/s e ",v*3.6,"km/h")
