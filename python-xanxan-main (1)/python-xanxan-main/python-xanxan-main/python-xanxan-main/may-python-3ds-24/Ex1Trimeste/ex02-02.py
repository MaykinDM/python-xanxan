print("Conversor de segundos em H:M:S.")
totalSegundos  =  int(input("informe o número total de segundos: "))
minutos = totalSegundos // 60
segundos = totalSegundos%60
horas=minutos // 60
minutos = minutos% 60
print(horas, ":", minutos,":", segundos)