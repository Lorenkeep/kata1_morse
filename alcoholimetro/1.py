
#Calcular la cantidad de gramos de alcohol

##gramosalcohol =  0 #gramos de alcohol ingeridos
##strVolumen = input("Introduce el volumen de alcohol ingerido") #volumen en centimetros cubicos de la bebida
##strGraduacion = input("¿Cuantos grados tiene la bebida que has tomado?")  #graduacion de la bebida alcoholica

##volumen = float(strVolumen)
##graduacion = float(strGraduacion)

##gramosalcohol = (volumen * graduacion) * 0.8 / 100

##print ("Has tomado {} gramos de alcohol".format(gramosalcohol))



def gramosAlcohol(volumen, graduacion):
    
    gramos = (volumen * graduacion) * 0.8 / 100
    return gramos

##gramosAlcohol(1000, 12)

print ("Llevas {} gramos de Alcohol en sangre".format(gramosAlcohol(1000, 12)))
