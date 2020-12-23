import tkinter as tk
from gopigo import*
from time import*


class Cadre(tk.Frame):
    def __init__(self, programme=None):
     tk.Frame.__init__(self,programme)
     self.place(width=1000, height=1000)

     self.B1 = tk.Button(self,text="^",command=self.avance)
     self.B1.place(x="50",y="450")
     
     self.B2=tk.Button(self,text="v",command=self.recule)
     self.B2.place(x="52",y="500")
     
     self.B3=tk.Button(self,text=">",command=self.droite)
     self.B3.place(x="70",y="475")
     
     self.B4=tk.Button(self,text="<",command=self.gauche)
     self.B4.place(x="35",y="475")

     self.B5=tk.Button(self,text="  ",command=self.stop)
     self.B5.place(x="52",y="475")

     self.B6=tk.Button(self,text="A",command=self.pilote_auto)
     self.B6.place(x="500",y="450")

     self.B7=tk.Button(self,text="     L1     ",command=self.accelerer)
     self.B7.place(x="40",y="100")

     self.B8=tk.Button(self,text="     L2     ",command=self.decelerer)
     self.B8.place(x="40",y="125")

     self.B9=tk.Button(self,text="     R1     ",command=self.increase_limit)
     self.B9.place(x="500",y="100")

     self.B10=tk.Button(self,text="     R2     ",command=self.decrease_limit)
     self.B10.place(x="500",y="125")

    limit=250
    
    def avance(self):
        servo(90)
        set_left_speed(160)
        set_right_speed(180)
        fwd()
        sleep(1)
        

    def recule(self):
        servo(90)
        set_left_speed(175)
        set_right_speed(180)
        bwd()
        sleep(1)
        

    def droite(self):
        servo(20)
        sleep(1)
        right_rot()
        sleep(0,10)
        stop()

    def gauche(self):
        servo(160)
        sleep(1)
        left_rot()
        sleep(0,1)
        stop()

    def stop(self):
        servo(90)
        stop()

    def accelerer(self):
        if left_speed<limit and right_speed<limit:
            increase_speed()
        else:
            print("Vitesse maximale atteinte")

    def decelerer(self):
        decrease_speed()

    def increase_limit:
        lim+=10

    def decrease_limit:
        lim-=10
    #-------------------------------------------------
        
    def reculer(r):
        bwd()
        sleep(r)
        stop()
        
        
    #-------------------------------------------------
        
    def droite(d):
        servo(20)
        sleep(1)
        right_rot()
        sleep(1)
        stop()
        print('Vous avez tournÃ© Ã  droite pendant',d,'sesondes')
    #-------------------------------------------------  
        
    def gauche(g):
        servo(160)
        sleep(1)
        left_rot()
        sleep(1)
        stop()
        print('Vous avez tournÃ© Ã  droite pendant',g,'sesondes')


    #-------------------------------------------------
    #Programme Principal
    #-------------------------------------------------
    def pilote_auto(self):
        def avancer(a):
            fwd()
            sleep(a)
        t3=0
        t1=time()
        d=us_dist(15)
        while(t3<20):
            servo(90)
            while(us_dist(15)>30):
                avancer(1)
            print(us_dist(15))

            stop()
            servo(5)
            sleep(0.2)
            d=us_dist(15)
            print("la distance droite est :", d)

            servo(90)
            sleep(0.2)

            servo(160)
            sleep(0.2)
            d1=us_dist(15)
            print("la distance gauche est :",d1)

            servo(90)
            sleep(0.2)


            if d>d1 :
                servo(5)
                sleep(1)
                right_rot()
                sleep(0.75)
                servo(90)
                while(us_dist(15)>40): 
                    avancer(1)
                stop()

            else:
                servo(160)
                sleep(1)
                left_rot()
                sleep(0.75)
                servo(90)
                while(us_dist(15)>40):   
                    avancer(1)
                stop()

            t2=time()
            print("t1:",t1,"t2",t2)
            t3=t2-t1
            print("t3=",t3)
            

        
        
           



prog = tk.Tk()
c = Cadre(prog)
prog.mainloop()
