txtseg = input("Por favor, entre com o número de segundos que deseja converter:")
seg = int(txtseg)

minutototal = seg//60
horas = minutototal//60
minutof = minutototal%60
segf = seg%60
dias = horas//24
horasf = horas%24
print (dias, "dias,", horasf, "horas,", minutof, "minutos e", segf, "segundos")
