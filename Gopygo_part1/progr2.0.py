from gopigo import *
from time import *
import turtle

set_right_speed(65)
set_left_speed(60)

def scan():
    enable_servo()
    angles=[]
    dist=[]
    distok=[]
    angle=0
    while (angle <= 175):
        servo(angle)
        dist.append(us_dist(15))
        sleep(0.3)
        angle+=10
        angles.append(angle)

    for i in range (0,18):
        if (dist[i]>=100):
            distok.append(i)
            turtle.color('green')
            turtle.forward(100)
            turtle.backward(100)
            turtle.left(10)
        else:
            turtle.color('red')
            turtle.forward(dist[i])
            turtle.backward(dist[i])
            turtle.left(10)
    print(distok)
    return(distok)
    
def detecter():
    servo(90)
    sleep(1)
    dist=us_dist(15)
    while (dist>30):
        avancer(1)
        dist=us_dist(15)
    if (dist<60):
        scan()
    newdir=int(input("Veuillez choisir la direction"))
    if (newdir<= 9):
        droite()
    if (newdir>9):
        gauche()
        
    


    
def avancer(tempsa):
    servo(90)
    sleep(1)
    fwd()
    sleep(tempsa)
    stop()
    print("le robot avance pendant",tempsa,"secondes")
    
def reculer(tempsr):
    bwd()
    sleep(tempsr)
    stop()
    print("le robot recule pendant",tempsr,"secondes")
    
def droite():
    right() 
    sleep(1)
    stop()
    print("le robot va tourner Ã  droite")
    
def gauche():
    left()
    sleep(1)
    stop()
    print("le robot va tourner Ã  gauche")
    
    
def avancerrot(n):
    t=n*18
    enc_tgt(1,1,t)
    fwd()

"""    
cont="oui"

while(cont=="oui" ):
    print("Bienvenu dans le menu de controle du robot")
    print("Vous pouvez choisir parmis les actions suivantes: avancer, reculer, droite, gauche")
    choix=(str(input("veuillez choisir l'action Ã  effectuer: ")))
    
    while (choix!="avancer") and (choix!="reculer") and (choix!="droite") and (choix!="gauche")and(choix!="detecter"):
        choix=(str(input("veuillez choisir l'action Ã  effectuer")))
        
    if (choix=="avancer"):
        tempsa=int(input("combien de temps voulez vous avancer ?"))
        avancer(tempsa)
    
    if (choix=="reculer"):
        tempsr=int(input("combien de temps voulez vous reculer ?"))
        reculer(tempsr)  
        
    if (choix=="gauche"):
        tempsg=int(input("combien de temps voulez vous tourner Ã  gauche ?"))
        gauche(tempsg)
        
    if (choix=="droite"):
        tempsd=int(input("combien de temps voulez vous tourner Ã  droite ?"))
        droite(tempsd)

    if (choix=="detecter"):
        detecter()

        
    cont=input("voulez vous retourner au menu ?")
while(cont!="oui" and cont!="non" ):
    cont=input("voulez vous retourner au menu (oui/non)?")
"""
k=0
while (k<=5):
    detecter()
    k+=1
    
    
