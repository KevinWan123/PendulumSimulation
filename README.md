# PendulumSimulation
<img src="SpiderManIcon!.png"></img>


# Introduction
<p>Hello! My name is Kevin, and I am presenting my Double Pendulum Project. Through this project, I have gained a deeper understanding of physics, as well as developed skills in GUI building and programming. I created this project with the goal of visually demonstrating the motion of a double pendulum while also allowing others to easily explore and experiment with it.</p>

## Here is a video showing how my program works.
[![Double Pendulum Simulation Program](https://img.youtube.com/vi/-DgiQJnjSQc/0.jpg)](https://www.youtube.com/watch?v=-DgiQJnjSQc)
<p>To begin this project, I utilized my knowledge of dynamics to systematically solve for the trajectory of a double pendulum.</p>
Here is an image of a double pendulum.
<img src= "http://rotations.berkeley.edu/wp-content/uploads/2017/10/double-pendulum.png"></img>


# How I solved the Double Pendulum

First, I need obtain the x and y values of each pendulum. To do this I used trigonomtry to find all the lengths.
$x_1= l_1sin(\theta_1)$ , $x_2= x_1+l_2sin(\theta_2)$, $y_1= -l_2cos(\theta_2)$ , $y_2= y_1-l_2sin(\theta_2)$

Next, I can find the velocity by taking the derivative


- $x_1'= \theta_1'l_1sin(\theta_1)$
- $y_1'=\theta_1l_1sin(\theta_1)$
- $x_2'= x_1'+\theta_2'l_2cos(\theta_2)$
- $y_2'=y_1'+\theta_2'l_2sin(\theta_2)$

And acceleration by taking the derivative of the velocity using the product rule

- $x_1''= -\theta_1'^2 l_1\sin(\theta_1)+\theta_1''l_1sin(\theta_1)$
- $y_1''=\theta_1'^2 l1cos(\theta_1)+\theta_1''l_1sin(\theta_1)$
- $x_2''= x_1'' - \theta_2'^2 l_2sin(\theta_2)+\theta_2''l_2cos(\theta_2)$
- $y_2''=y_1''+\theta_2'' l_2cos(\theta_2)+\theta_2''l_2sin(\theta_2)$

Next, I used Newton's Second Law F= MA. I drew the free body diagram.
# FBD 1
<img src =
"https://www.myphysicslab.com/pendulum/dbl_pendulum_m1.gif"></img>

# FBD 2
<img src =
"https://www.myphysicslab.com/pendulum/dbl_pendulum_m2.gif"></img>



As you see, in pendulum 1, there are 3 forces, T1, T2,and M1g.
I can model the equation of motion with the following equation:

- $m_1 x_1'' = -T_1sin(\theta_1)+T_2sin(\theta_2)$
- $m_1 y_1''=T_1cos(\theta_1)-T_2cos(\theta_2)-m_1g$

Looking at FBD for pendulum 2, there are only 2 forces, T2 and Mg.I can model the equation of motion for pendulum 2 with the following equation:

- $m_2x_2''=-T_2sin(\theta_2)$
- $m_2y_2''=T_2cos(\theta_2)-m_2g$

With the equations of motion, we can solve this by inputting the initial conditions. My initial conditions were,
$\theta_1=0$, $\theta_2=90$, $\omega_1 =0$, $\omega_2=0$. My length 1, length 2, mass 1, mass 2 are all adjustable in the program
You can also use the langrangian method to solve this. In my Code I used the Runge Kutta to solve the equation of motion numerically, it involves approximating the solution using a weighted average of several estimates of the derivative at different points within each time step.

# My program with Pictures
Booting up the program it will look like this
![image](https://user-images.githubusercontent.com/114878518/206978950-b03af6f0-7250-49ef-9239-151cca20cc57.png)

By pressing start it will enter the default value and run the animation for 20 seconds
![image](https://user-images.githubusercontent.com/114878518/206979120-05fc30c1-259c-4030-9609-186047c22c45.png)

Using the time slider you can change the speed of the simulation
![image](https://user-images.githubusercontent.com/114878518/206979188-cd8e122a-5b6a-4d14-a787-0eb602663194.png)

You can enter any mass or length you want!
![image](https://user-images.githubusercontent.com/114878518/206979256-d3aca0f8-1cc7-4723-8dc6-a6b224e90353.png)
![image](https://user-images.githubusercontent.com/114878518/206979339-b148a76b-cb3b-4c7c-92f0-f4497a391e4e.png)

But make sure you don't input a letter or 0
![image](https://user-images.githubusercontent.com/114878518/206979409-e9ff02c2-7079-4b26-bd4b-b2f000a49fed.png)


# Download
https://drive.google.com/file/d/10uA-E2KgR_26YAgyNcJ6FwgAgiqi3zzV/view?usp=sharing



  
# Acknowledgement
- [Professor Ryan Cooper](https://github.com/cooperrc)
- [Gabriel Koleszar](https://github.com/gabekole)

