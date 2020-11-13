#CALCULADORA GRAVITACIONAL
# k é a constante gravitacional e f fórmula
#rt o raio da terra e mt a massa da terra
while True:
 k = (6.7/(10**11))
 rt = ((6.37)*(10**6))
 mt = ( 5.98*(10**24))

 def aceleracaodagravidade():
     m = int (input  ("Massa do planeta:"))
     r = int (input  ("Raio do planeta:"))
     f =(k*m)/(r**2)
     return print("A aceleração é",f,"m/s^2")
 
 def forcagravitacional():
     m1 = int (input  ("Massa 1:"))
     m2 = int (input  ("Massa 2:"))
     r = int (input  ("Distância entre as duas massas:"))
     f=(k*m1*m2)/(r**2)
     return  print("A força é de ",f,"N")
 
 def velocidadedesatelite():
     print("velocidade de um satélite na órbita terrestre")
     h = int ( input  ("Altura do do satélite :"))
     f = ((k*mt)/((rt+h)**2))**1/2
     return print("A velocidade é",f,"m/s e ",f*3.6,"km/h")

 def periodosatelite():
    h = int ( input  ("Altura do satélite:"))
    f = (4*((3.14)**2)*((rt+h)**3)/(k*mt))**1/2
    return print("o período é de",f,"segundos")

 def velocidadedeescape():
      m = int  ( input ("Massa do planeta:"))
      r = int ( input  ("Raio do planeta :"))
      f=(2*k*m/r)**1/2
      return print  ("A velocidade de escape é ",f,"m/s ou",f*3.6,"km/h")
	  
 def menu():
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
   x = input("DIGITE A OPÇÃO:")
   if x.isdigit()==False:
    	print("USE APENAS OS NÚMEROS DA TELA PRINCIPAL")
    	menu()
   else:
        n=int(x)
        if n>5 or n<0:
         print("comando inválido!")
        if n==1:
          aceleracaodagravidade()
        if n==2:
          forcagravitacional()
        if n==3:
          velocidadedesatelite()
        if n==4:
          periodosatelite()
        if n==5:
          velocidadedeescape()
        if n==0:
         exit()
 menu()
