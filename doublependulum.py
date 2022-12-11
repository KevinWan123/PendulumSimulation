from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from tkinter import *
import scipy.integrate as integrate
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




window = Tk()
window.geometry("900x800")
window.title("Double Pendulum")

class App():
    def __init__(self,master):

        #Figure
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
        self.ax.grid()
        self.plot1 = FigureCanvasTkAgg(self.fig, master=window).get_tk_widget()
    
        #Setting up GUI
        self.G = 9.81
        self.mass1 = IntVar()
        self.mass1Label = Label(window, text="Mass 1:")
        self.mass1Entry = Entry(window,textvariable= self.mass1)
        self.mass1.set(1)
        self.mass2= IntVar()
        self.mass2Label = Label(window,text="Mass 2:")
        self.mass2Entry = Entry(window,textvariable=self.mass2)
        self.mass2.set(1)
        self.length1 = IntVar()
        self.length1Label = Label(window, text= "Length 1:")
        self.length1Entry = Entry(window, textvariable=self.length1)
        self.length1.set(1)
        self.length2 = IntVar()
        self.length2Label = Label(window, text= "Length 2:")
        self.length2Entry = Entry(window, textvariable=self.length2)
        self.length2.set(1)
        self.startb = Button(window,text="Start", command = self.start)
        self.startb.place(relx = .3,rely=.9 )
        self.stopb = Button(window, text="Stop", command = self.stop)
        self.stopb.place(relx=.5, rely = .9)
        self.name = Label(window,text="Created by Kevin Wan")
        self.name.place(relx =.7, rely=.9)

        

        #Place Variables
        print("variables")
        self.mass1Entry.place(relx =.05,rely =.7)
        self.mass2Entry.place(relx =.35,rely =.7)
        self.length1Entry.place(relx=.60, rely=.7)
        self.length2Entry.place(relx=.80 , rely=.7)
        self.mass1Label.place(relx=0,rely=.7)
        self.mass2Label.place(relx=.28,rely=.7)
        self.length1Label.place(relx=.52,rely=.7)
        self.length2Label.place(relx=.72,rely=.7)
        self.plot1.place(relx=.1,rely=0)


        #Time Array
        self.dt = 0.05
        self.t = np.arange(0.0, 20, self.dt)


        #Initial Angular Velocity
        self.th1 = 0
        self.w1 = 0.0
        self.th2 = 90
        self.w2 = 0.0

        # # initial state
        self.state = np.radians([self.th1, self.w1, self.th2, self.w2])

        self.line, = self.ax.plot([], [], 'o-', lw=2)
        self.time_template = 'time = %.1fs'
        self.time_text = self.ax.text(0.05, 0.9, '', transform=self.ax.transAxes)


        #Integration
        self.y = integrate.odeint(self.derivs, self.state, self.t)

        self.x1 = self.length1.get()*sin(self.y[:, 0])
        self.y1 = -self.length1.get()*cos(self.y[:, 0])

        self.x2 = self.length2.get()*sin(self.y[:, 2]) + self.x1
        self.y2 = -self.length2.get()*cos(self.y[:, 2]) + self.y1

        #Animation
        self.ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, len(self.y)),
                               interval=25, blit=False, init_func=self.init)

        self.k = 0

        #start
    def start(self):

        try:
           

            self.l1= self.length1.get()
            self.l2 = self.length2.get()
            self.m1 = self.mass1.get()
            self.m2 = self.mass2.get()

            self.y = integrate.odeint(self.derivs, self.state, self.t)

            self.x1 = self.l1*sin(self.y[:, 0])
            self.y1 = -self.l1*cos(self.y[:, 0])

            self.x2 = self.l2*sin(self.y[:, 2]) + self.x1
            self.y2 = -self.l2*cos(self.y[:, 2]) + self.y1

            self.k = 1
            self.ani.event_source.start() 

        except:
            self.stop()
    
    def stop(self):
        self.k = 0
        return self.k
        


        

    def init(self):
        self.line.set_data([], [])
        self.time_text.set_text('')
        return self.line, self.time_text
  

    def animate(self,i):

        

        if self.k == 0:
            self.ani.event_stop.stop()
        else:
            #Resize window due to change in length
            value = max([self.l1+1,self.l2+1])
            self.ax.set_xlim(-value, value)
            self.ax.set_ylim(-value,value)
            
            
            
    
            
           
            thisx = [0, self.x1[i], self.x2[i]]
            thisy = [0, self.y1[i], self.y2[i]]

            self.line.set_data(thisx, thisy)
            self.time_text.set_text(self.time_template % (i*self.dt))

           
            return self.line, self.time_text

    def derivs(self,state, t):
        try:
            th1 = state[0] 
            w1 = state[1]
            th2 = state[2] 
            w2 = state[3]

            dydx = np.zeros_like(state)
            dydx[0] = w1

            del_ = th2 - th1
            den1 = (self.m1+ self.m2)*self.l1 - self.m2*self.l1*cos(del_)*cos(del_)
            dydx[1] = (self.m2*self.l1*(w1**2)*sin(del_)*cos(del_) +
                    self.m2*self.G*sin(th2)*cos(del_) +
                    self.m2*self.l2*(w2**2)*sin(del_) -
                    (self.m1 + self.m2)*self.G*sin(th1))/den1

            dydx[2] = w2

            den2 = (self.l2/self.l1)*den1
            dydx[3] = (-self.m2*self.l1*(w2**2)*sin(del_)*cos(del_) +
                    (self.m1 + self.m2)*self.G*sin(th1)*cos(del_) -
                    (self.m1 + self.m2)*self.l1*(w1**2)*sin(del_) -
                    (self.m1 + self.m2)*self.G*sin(th2))/den2
        except:
            th1 = state[0] 
            w1 = state[1]
            th2 = state[2] 
            w2 = state[3]

            dydx = np.zeros_like(state)
            dydx[0] = w1

            del_ = th2 - th1
            den1 = (self.mass1.get()+ self.mass2.get())*self.length1.get() - self.mass2.get()*self.length1.get()*cos(del_)*cos(del_)
            dydx[1] = (self.mass1.get()*self.length1.get()*(w1**2)*sin(del_)*cos(del_) +
                    self.mass2.get()*self.G*sin(th2)*cos(del_) +
                    self.mass2.get()*self.length2.get()*(w2**2)*sin(del_) -
                    (self.mass1.get() + self.mass2.get())*self.G*sin(th1))/den1

            dydx[2] = w2

            den2 = (self.length2.get()/self.length1.get())*den1
            dydx[3] = (-self.mass2.get()*self.length1.get()*(w2**2)*sin(del_)*cos(del_) +
                    (self.mass1.get() + self.mass2.get())*self.G*sin(th1)*cos(del_) -
                    (self.mass1.get() + self.mass2.get())*self.length1.get()*(w1**2)*sin(del_) -
                    (self.mass1.get() + self.mass2.get())*self.G*sin(th2))/den2


        return dydx
    
 
    
            



App(window)
mainloop()