import random
import time
def mis_dados():
    
    n=random.randint(1, 6)
    m=random.randint(1, 6)
    resp=(input("Quieres tirar los dados (s/n) : "  ))
    mi_apuesta=float(input("Cuanto quieres apostar?: "))
    time.sleep(2)
   
    suma=n+m

    while resp == "s":
        

           print(n, m,"= ", suma)
           break  
    while resp == "n":
    

          print("Vuelva cuando quiera")
          break       
    
    
    time.sleep(1) 
          
    if (suma == 7 or suma == 11):
        print("Todos ganan por el doble")

    elif (suma ==2 or suma == 6 or suma == 12):
        print("Jugador gana por cuatro")
        
    else:
        print("Siga probando")   
        

    while (suma == 7 or suma == 11):
        mi_apuesta=mi_apuesta*2
        print("Ganas: ", mi_apuesta )
        break

    while (suma ==2 or suma == 6 or suma == 12):
        mi_apuesta=mi_apuesta*4
        print("Ganas:", mi_apuesta)
        break
    mis_dados()

mis_dados()

