#CALCULADORA GRAVITACIONAL
def a():
   k = (6.7/(10**11))
   return (k*m)/(r**2)
def b():
   k = (6.7/(10**11))
   return (k*m1*m2)/(r**2)
def c():
   r = ((6.37)*(10**6))
   m = ( 5.98*(10**24))
   k = (6.7/(10**11))
   return ((k*m)/((r+h)**2))**1/2
def d():
	  r = ((6.37)*(10**6))
	  k = (6.7/(10**11))
	  m = ( 5.98*(10**24))
	  return (4*((3.14)**2)*((r+h)**3)/(k*m))**1/2
def e():
	  k = (6.7/(10**11))
	  return (2*k*m/r)**1/2
print("""CALCULADORA GRAVITACIONAL:
          1-gravidade de um planeta
          2-força gravitacional entre
          dois corpos
          3-velocidade de um satélite
          4-período de um satélite 
          5-velocidade de escape de
          um planeta
          0-sair
          obs: use unidades em kg e m""")
n = int(input ("Escolha:"))
if n>5 or n<0:
	  print  ("comando inválido!")
if n==1:
   m = int (input  ("Massa do planeta:"))
   r = int (input  ("Raio do planeta:"))
   print("A aceleração é",a(),"m/s^2")
if n==2:
 m1 = int (input  ("Massa 1:"))
 m2 = int (input  ("Massa 2:"))
 r = int (input  ("Distância entre as duas massas:"))
 print("A força é de ",b(),"N")
if n==3:
   print("velocidade de um satélite na órbita terrestre")
   h = int ( input  ("Altura do do satélite :"))
   print("A velocidade é",c(),"m/s e ",c()*3.6,"km/h")
if n==4:
  h = float  ( input  ("Altura do satélite:"))
  print("o período é de",d(),"segundos")
if n==5:
   m = int  ( input ("Massa do planeta:"))
   r = int ( input  ("Raio do planeta :"))
   print  ("A velocidade de escape é ",e(),"m/s ou",e()*3.6,"km/h")
if n==0:
	exit ()
