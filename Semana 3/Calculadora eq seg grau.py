import math

a = float(input("Digite o termo que acompanha x^2:"))
b = float(input("Digite o termo que acompanha x:"))
c = float(input("Digite o termo independente:"))

delta = b**2 - 4*a*c


if delta < 0:
    print("esta equação não possui raízes reais")
    
else:
    y = math.sqrt(delta)

if delta == 0:
    x = (- b)/(2*a)
    print ("a raiz desta equação é", x)
    
if delta > 0:
    x1 = (-b + y)/(2*a)
    x2 = (-b - y)/(2*a)
    if x1 > x2:
        print ("as raízes da equação são", x2, "e", x1)
    else:
        print ("as raízes da equação são", x1, "e", x2)
  
        
