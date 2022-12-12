from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from tkinter import *
import scipy.integrate as integrate
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Code create by Kevin Wan for CE2120
plt.style.use('dark_background') #Configure plot style. I personally like dark mode



window = Tk()
window.iconbitmap('SpiderManIcon!.ico')
window.geometry("900x800")
window.title("Double Pendulum")
window.configure(bg='black')





class App():
    def __init__(self,master):
       


        #Figure
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
        self.ax.grid(False) # Remove gridlines
        #self.ax.axis('off') #if you want like a youtube video type of look
        #Removing right and top spine
        self.ax.spines.right.set_visible(False)
        self.ax.spines.top.set_visible(False)
        self.ax.set_title("Double Pendulum Simulation")
        # self.ax.spines.bottom.set_visible(False)
        # self.ax.spines.left.set_visible(False)



        self.plot1 = FigureCanvasTkAgg(self.fig, master=window).get_tk_widget()


        #Canvas 
        self.w = Canvas(window,bg="#2d3033",bd=0,relief='ridge',highlightthickness=0)
     
        self.w.place(relx=0,rely=.6,relwidth=2,relheight=2)
        
        
    
        #Setting up GUI
        self.G = 9.81
        self.mass1 = StringVar()
        self.mass1Label = Label(window, text="Mass 1:", bg="#a2dbd7",highlightthickness=0,bd=0,height=1,font=("Didot",12))
        self.mass1Entry = Entry(window,textvariable= self.mass1,bg="#89b340",highlightthickness=0,bd=0,font=("Didot",12),width=10)
        
        self.mass1.set(1)
        self.mass2= StringVar()
        self.mass2Label = Label(window,text="Mass 2:",bg="#a2dbd7",highlightthickness=0,bd=0,height=1,font=("Didot",12))
        self.mass2Entry = Entry(window,textvariable=self.mass2,bg="#89b340",highlightthickness=0,bd=0,font=("Didot",12),width=10)
        self.mass2.set(1)
        self.length1 = StringVar()
        self.length1Label = Label(window, text= "Length 1:",bg="#a2dbd7",highlightthickness=0,bd=0, height=1,font=("Didot",12))
        self.length1Entry = Entry(window, textvariable=self.length1,bg="#89b340",highlightthickness=0,bd=0,font=("Didot",12),width=10)
        self.length1.set(1)
        self.length2 = StringVar()
        self.length2Label = Label(window, text= "Length 2:",bg="#a2dbd7",highlightthickness=0,bd=0,height =1,font=("Didot",12))
        self.length2Entry = Entry(window, textvariable=self.length2,bg="#89b340",highlightthickness=0,bd=0,font=("Didot",12),width=10)
        self.length2.set(1)
        self.startb = Button(window,text="Start", command = self.start,bg='#2d3033',fg='Green',font=("Roboto",24),highlightcolor='lightgray',cursor="spider")
        self.startb.place(relx = .3,rely=.9 )
        self.stopb = Button(window, text="Stop", command = self.stop,bg='#2d3033',fg='Red',font=("Roboto",24),highlightcolor='lightgray',cursor='spider')
        self.stopb.place(relx=.5, rely = .9)
        self.name = Label(window,text="Created by Kevin Wan", font=('Roboto',18) ,fg='White', bg='#2d3033',cursor="spider")
        self.name.place(relx =.7, rely=.9)

        

        #Place Variables
        print("variables")
        self.mass1Entry.place(relx =.11,rely =.7)
        self.mass2Entry.place(relx =.36,rely =.7)
        self.length1Entry.place(relx=.61, rely=.7)
        self.length2Entry.place(relx=.86 , rely=.7)

        self.mass1Label.place(relx=.05,rely=.7)
        self.mass2Label.place(relx=.3,rely=.7)
        self.length1Label.place(relx=.54,rely=.7)
        self.length2Label.place(relx=.79,rely=.7)
        self.plot1.place(relx=.15,rely=0)



        #Time Array
        self.dt = 0.05 #Change speed of simulation
        self.t = np.arange(0.0, 20, self.dt)

        #Time slider
        self.timeLabel = Label(window,text="Time Slider: ",font=("Roboto",24),bg='#2d3033',fg='White')
        self.timeLabel.place(relx=.25,rely=.8)
        self.time= StringVar()
        self.time.set(.05)
        slider= Scale(window,from_=.01,to_=.05,orient='horizontal',resolution=.01,variable=self.time,bg="#3e6f70",font=("Roboto",10),cursor="spider")
        slider.place(relx=.5,rely=.8)


        #Initial Angular Velocity and angles
        self.th1 = 0
        self.w1 = 0.0
        self.th2 = 90
        self.w2 = 0.0

        # # initial state
        self.state = np.radians([self.th1, self.w1, self.th2, self.w2])

        self.line, = self.ax.plot([], [], 'o-', lw=2)
        self.trace, = self.ax.plot([], [], '.-', lw=1, ms=2)
        self.line.set_color("fuchsia")


        self.time_template = 'time = %.1fs'
        self.time_text = self.ax.text(0.05, 0.9, '', transform=self.ax.transAxes)



        #Integration
        self.y = integrate.odeint(self.derivs, self.state, self.t)

        self.x1 = float(self.length1.get())*sin(self.y[:, 0])
        self.y1 = -float(self.length1.get())*cos(self.y[:, 0])

        self.x2 = float(self.length2.get())*sin(self.y[:, 2]) + self.x1
        self.y2 = -float(self.length2.get())*cos(self.y[:, 2]) + self.y1

        #Animation
        self.ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, len(self.y)),
                               interval=25, blit=False, init_func=self.init)

        self.k = 0

        #start
    def start(self):
        #Thinking of adding error cases to try and except


        try:
            
            self.dt = float(self.time.get()) #Change speed of simulation
            self.t = np.arange(0.0, 20, self.dt)
           
            #If user changes lenngth, then the change will show up on animation due to setting the variable to the input boxes.
            self.l1= float(self.length1.get())
            self.l2 = float(self.length2.get())
            self.m1 = float(self.mass1.get())
            self.m2 = float(self.mass2.get())


            self.y = integrate.odeint(self.derivs, self.state, self.t)

            self.x1 = self.l1*sin(self.y[:, 0])
            self.y1 = -self.l1*cos(self.y[:, 0])

            self.x2 = self.l2*sin(self.y[:, 2]) + self.x1
            self.y2 = -self.l2*cos(self.y[:, 2]) + self.y1

            self.k = 1
            self.ani.event_source.start() 

        except:
            #If user makes an error like entering a string spawn a message
            print('Enter an float value')
            self.stop()
    
    def stop(self):
        #Set k to zero to stop animation
        self.k = 0
        return self.k
        


        

    def init(self):
        self.line.set_data([], [])
        self.time_text.set_text('')
        return self.line, self.time_text
  

    def animate(self,i):

        

        if self.k == 0: #If k is 0, then stop animation
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
            # self.trace.set_data(self.history_x,self.history_y)

           
            return self.line,self.time_text

    def derivs(self,state, t):
        #The reason there is a try except here is because the derivs function needs to be ran before the start button can be pressed and the start function is where we initialize l1,l2,m1,m2``. That means we haven't initialized l1,l2,m1,m2 yet. But once we do we need to use l1,l2 instead of length1,length2
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
            den1 = (float(self.mass1.get())+ float(self.mass2.get()))*float(self.length1.get()) - float(self.mass2.get())*float(self.length1.get())*cos(del_)*cos(del_)
            dydx[1] = (float(self.mass1.get())*float(self.length1.get())*(w1**2)*sin(del_)*cos(del_) +
                    float(self.mass2.get())*self.G*sin(th2)*cos(del_) +
                    float(self.mass2.get())*float(self.length2.get())*(w2**2)*sin(del_) -
                    (float(self.mass1.get()) + float(self.mass2.get()))*self.G*sin(th1))/den1

            dydx[2] = w2

            den2 = (float(self.length2.get())/float(self.length1.get()))*den1
            dydx[3] = (-float(self.mass2.get())*float(self.length1.get())*(w2**2)*sin(del_)*cos(del_) +
                    (float(self.mass1.get())+ float(self.mass2.get()))*self.G*sin(th1)*cos(del_) -
                    (float(self.mass1.get())+ float(self.mass2.get()))*float(self.length1.get())*(w1**2)*sin(del_) -
                    (float(self.mass1.get()) + float(self.mass2.get()))*self.G*sin(th2))/den2


        return dydx
    
 
    
            



App(window)
mainloop()