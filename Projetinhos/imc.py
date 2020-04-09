x = input ("Qual o seu peso em kg?")
y = input ("Qual sua altura em m?")

peso = float(x)
altura = float (y)

imc = peso/(altura**2)

print ("seu IMC é:", imc)
