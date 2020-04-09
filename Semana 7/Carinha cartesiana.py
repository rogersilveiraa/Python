
eixo_x = 5
eixo_y = 7


while eixo_y >= 0:

    while eixo_x > -5:
        if eixo_y < 1:
            print ("#", end= "")
            
        elif eixo_y < 2 and ( eixo_x <= -3 or eixo_x > 3):
            print ("#", end= "")

        elif eixo_y < 2:
            print (" ", end= "")

        elif eixo_y < 4:
            print ("#", end= "")

        elif eixo_y < 5 and (eixo_x <= -4 or ( eixo_x > -1 and eixo_x <= 1) or eixo_x > 4):
            print ("#", end= "")

        elif eixo_y < 5:
            print (" ", end= "")

        elif eixo_y < 6 and (eixo_x <= -4 or (eixo_x > -3 and eixo_x <= -2) or (eixo_x > -1 and eixo_x <= 1) or (eixo_x > 2 and eixo_x <= 3) or eixo_x > 4):
            print ("#", end= "")

        elif eixo_y < 6:
            print (" ", end= "")

        elif eixo_y < 7 and (eixo_x <= -4 or ( eixo_x > -1 and eixo_x <= 1) or eixo_x > 4):
            print ("#", end= "")

        elif eixo_y < 7:
            print (" ", end = "")

        else:
            print("#", end = "")

        eixo_x -=1
        
    print ()
    eixo_y -=1
    eixo_x = 5

x = 10
y = 10

while not(x <= 5 and x >= -4 and y <= 7 and y >= 0):
    print ("Digite um ponto cartesiano para saber o que há nele")
    x = int(input("Digite o ponto do eixo X, 5 >= x >= -4: \n"))
    y = int(input("Digite o ponto do eixo Y, 7 >= y >= 0: \n"))
    
if y < 1:
    ponto = True
               
elif y < 2 and ( x <= -3 or x > 3):
    ponto = True
           
elif y < 2:
    ponto = False            

elif y < 4:
    ponto = True           

elif y < 5 and (x <= -4 or ( x > -1 and x <= 1) or x > 4):
    ponto = True

elif y < 5:
    ponto = False          

elif y < 6 and (x <= -4 or (x > -3 and x <= -2) or (x > -1 and x <= 1) or (x > 2 and x <= 3) or x > 4):
    ponto = True

elif y < 6:
    ponto = False

elif y < 7 and (x <= -4 or ( x > -1 and x <= 1) or x > 4):
    ponto = True

elif y < 7:
    ponto = False

else:
    ponto = True
            
if ponto == True:
    ponto = "esta marcado com #"
else:
    ponto = "está marcado com ' ' "

print (" O ponto (", x, ",", y, ")", ponto)

