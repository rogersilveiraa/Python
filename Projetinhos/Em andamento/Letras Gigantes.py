def main ():
    
    entrada = input("Digite uma palavra")

    palavra = []

    for letter in entrada:
        palavra.append (letter)

    contador = 0

    while contador < len(palavra):
        letra = palavra[contador]

        if letra == ("a" or "A"):
            desenho = a()
        
        elif letra == ("b" or "B"):
            b()
        print ()
        contador += 1
        
def a():

    y = 8

    while y > 0:

        x = 1

        while x < 7:

            if y == 8 and (x == 3 or x == 4):
                print ("#", end = "")

            elif y == 8:
                print (" ", end = "")

            elif y == 7 and ( x >= 2 and x <=5):
                print ("#", end = "")
                
            elif y == 7:
                print (" ", end = "")

            elif (y == 6 or y == 5 or y == 2 or y == 1) and (x == 1 or x == 2 or x == 5 or x == 6):
                print ("#", end = "")

            elif y == 6 or y ==5 or y == 2 or y == 1:
                print (" ", end = "")

            else:
                print ("#", end = "")

            x += 1
        print()
        y -= 1

def b ():

    y = 8

    while y > 0:

        x = 1

        while x < 7:

            if (y == 8 or y == 1 or y == 5) and x != 6:
               print ("#", end = "")

            elif y == 8 or y == 1:
                print (" ", end = "")

            elif y == 7 or y == 4 or y == 2:
                print ("#", end = "")

            elif (y == 6 or y ==3) and ( x != 3 and x != 4):
                print ("#", end = "")

            else:
                print (" ", end = "")

            x += 1

        print ()
        y -= 1

######
######
##
##
##
##
######
######

#####
######
##  ##
##  ##
##  ##
##  ##
######
#####

######
######
##
#####
#####
##
######
######

######
######
##
#####
#####
##
##
##

######
######
##
## 
## ###
##  ##
######
######

##  ##
##  ##
##  ##
######
######
##  ##
##  ##

  ##
  ##

  ##
  ##
  ##
  ##
  ##

######
######
   ##
   ##
   ##
## ##
## ##
 ###

##  ##
##  ##
## ##
#####
#####
## ##
##  ##
##  ##

 
 ###  ###
##  ##  ##
##  ##  ##
##  ##  ##
##  ##  ##
##  ##  ## 9 x 6 


####   ##
#####  ##
## ##  ##
##  ## ##
##  ##### 9 x6 
##  ####   
