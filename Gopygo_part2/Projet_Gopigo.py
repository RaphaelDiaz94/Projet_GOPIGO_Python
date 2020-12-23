""" Ce code m'a servit l'année dernière dans le cadre d'un projet de programmation.
Nous avions un robot motorisé à notre disposition et nous devions le faire évoluer dans un espace, de manière commandée ou automatique,
sans qu'il ne heurte d'obstacle.
Lorsque le programme démarrait, une interface graphique apparaissait.
Cette dernière était composée de boutons sur lesquels nous pouvions cliquer pour interagir avec le robot.
Nous y avons rajouté un système empêchant à tout moment le robot de rentrer dans un mur ainsi qu'un limiteur de vitesse et un mode de pilote automatique. """


import tkinter as tk
from threading import Thread
from time import*
from gopigo import* #bibliothèque spécifique au robot utilisé  pour le projet

global ok
ok=1
class fond(Thread):  #création de la classe de fond anti-collision
    
    def __init__(self):
        
        Thread.__init__(self)
        
    def run(self):
        global ok
        d=us_dist(15)
        while ok==1:   
            if d>50:
                d=us_dist(15)
                
            if d<50 :
                stop()
                d=us_dist(15)
    
        

class Cadre(tk.Frame): #création de l'interface graphique contenant les diférents boutons
    def __init__(self, programme=None):
     tk.Frame.__init__(self,programme)
     self.place(width=300, height=230)
     self["bg"]=("silver")

     self.B1 = tk.Button(self,text="^",command=self.avance)
     self.B1.place(x="34",y="150")
     self.B1["bg"]=("grey")
     
     self.B2=tk.Button(self,text="v",command=self.recule)
     self.B2.place(x="35",y="200")
     self.B2["bg"]=("grey")
     
     self.B3=tk.Button(self,text=">",command=self.droite)
     self.B3.place(x="53",y="175")
     self.B3["bg"]=("grey")
     
     self.B4=tk.Button(self,text="<",command=self.gauche)
     self.B4.place(x="18",y="175")
     self.B4["bg"]=("grey")

     self.B5=tk.Button(self,text="  ",command=self.stop)
     self.B5.place(x="36",y="175")
     self.B5["bg"]=("red")

     self.B6=tk.Button(self,text="A",command=self.pilote_auto)
     self.B6.place(x="220",y="175")
     self.B6["bg"]=("gold")

     self.B7=tk.Button(self,text="     L1     ",command=self.accelerer)
     self.B7.place(x="20",y="20")
     self.B7["bg"]=("blue")

     self.B8=tk.Button(self,text="     L2     ",command=self.decelerer)
     self.B8.place(x="20",y="45")
     self.B8["bg"]=("orange")

     self.B9=tk.Button(self,text="     R1     ",command=self.increase_limit)
     self.B9.place(x="200",y="20")
     self.B9["bg"]=("blue")

     self.B10=tk.Button(self,text="     R2     ",command=self.decrease_limit)
     self.B10.place(x="201",y="45")
     self.B10["bg"]=("orange")

     self.B11=tk.Button(self,text=" stop thread ",command=self.stop_thread)
     self.B11.place(x="100",y="20")
     self.B11["bg"]=("red")

     global limit
     limit=200
     global Lspeed
     Lspeed=175
     global Rspeed
     Rspeed=183
     
    def avance(self):
        global ok
        ok=1
        servo(90) #place le servo-moteur droit afin de pouvoir mesurer la distance restant devant lui
        thread__fond = fond()
        thread__fond.start()#lancement de la classe de fond anti-collision
        print("avance: ok=",ok)
        set_left_speed(175)
        set_right_speed(183)
        fwd()
             

    def recule(self):
        global ok
        ok=0
        print("ok:",ok)
        servo(90)
        set_left_speed(175)
        set_right_speed(175)
        bwd()
        sleep(1)
        

    def droite(self):
        servo(20) #le servo-moteur regarde à droite
        for j in range(0,3): #démarage du clignotant droit
            led_on(0)
            sleep(0.4)
            led_off(0)
            sleep(0.4)
        right_rot()
        sleep(0.535)
        stop()

    def gauche(self):
        servo(160)#le servo-moteur regarde à gauche
        for i in range(0,3):#démarage du clignotant gauche
            led_on(1)
            sleep(0.4)
            led_off(1)
            sleep(0.40)
        left_rot()
        sleep(0.515)
        stop()

    def stop(self):
        global ok
        ok=1
        print("stop: ok=",ok)
        servo(90)
        stop()
        

    def accelerer(self):
        global Lspeed
        global limit
        global Rspeed 
        if Lspeed<limit and Rspeed<limit:# vérification que la vitesse demandée est inférieure à celle du limiteur
            increase_speed()
            Lspeed+=10
            Rspeed+=10
            print("La vitesse du moteur droit est:", Rspeed)
            print("La vitesse du moteur gauche est:", Lspeed)
        else:
            print("Vitesse maximal atteinte")
        return(Lspeed,Rspeed)
        

    def decelerer(self):
        decrease_speed()

    def increase_limit(self):
        global limit
        limit+=10
        print("Le limiteur de vitesse est fixé à  : ",limit)
        return(limit)

    def decrease_limit(self):
        global limit
        global Lspeed
        global Rspeed 
        print("Le limiteur de vitesse est fixÃ© Ã  : ",limit)
        limit-=10
        if Lspeed>limit or Rspeed>limit: #si la vitesse du robot est supérieure à la nouvelle vitesse limite demandée, le robot ralenti
            decrease_speed()
            Lspeed-=10
            Rspeed-=10
            print("----------------------------")
            print("La nouvelle vitesse du moteur droit est:",Rspeed)
            print("La nouvelle vitesse du moteur gauche est:",Lspeed)
        
    #-------------------------------------------------
        
    def reculer(r):
        bwd()
        sleep(r)
        stop()
        print('Vous avez reculé pendant',r,'secondes')

    def stop_thread(self):
        global ok
        ok=0
        print("thread : ok=",ok)
        
    #-------------------------------------------------
            #Pilote automatique
    #-------------------------------------------------
    def pilote_auto(self):
        global ok
        ok=0
        import time
        def avancer(a):           
            servo(90)
            set_left_speed(175)
            set_right_speed(183)
            fwd()
            sleep(a)
    
        t3=0
        t1=time.time()
        d=us_dist(15)
        while(t3<45): #fixe la durée de fonctionnement du pilote automatique à 45 secondes
            servo(90)
            while(us_dist(15)>45): #vérifie qu'il a toujours la distance suffisante pour avancer
                avancer(1)
            print(us_dist(15))
            stop()
            servo(5)
            sleep(1)
            d=us_dist(15)
            print("la distance droite est :", d)#mesure et enregiste la distance à droite

            servo(90)
            sleep(0.5)

            servo(160)
            sleep(1)
            d1=us_dist(15)
            print("la distance gauche est :",d1)#mesure et enregiste la distance à gauche

            servo(90)
            sleep(0.5)


            if d>d1 : #choisi la meilleur direction à prendre
                servo(5)
                sleep(1)
                for j in range(0,3):
                    led_on(0)
                    sleep(0.4)
                    led_off(0)
                    sleep(0.4)
                right_rot()
                sleep(0.45)
                servo(90)
                while(us_dist(15)>40): 
                    avancer(1)
                stop()

            else:
                servo(160)
                sleep(1)
                for i in range(0,3):
                    led_on(1)
                    sleep(0.4)
                    led_off(1)
                    sleep(0.4)
                left_rot()
                sleep(0.40)
                servo(90)
                while(us_dist(15)>40):   
                    avancer(1)
                stop()

            t2=time.time()
            print("t1:",t1,"t2",t2)
            t3=t2-t1
            print("t3=",t3)
        
    thread__fond = fond()
    thread__fond.start()
    
    

prog = tk.Tk()
prog.geometry("300x230") #dimension de l'interface graphique
c = Cadre(prog)
prog.mainloop()  


