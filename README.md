# PendulumSimulation
<img src="SpiderManIcon!.png"></img>


# Introduction
<p>Hello! My name is Kevin and this is my Double Pendulum Project. While doing this project, I have learned so much about physics, gui building, and programming in general. I wanted to capture the motion of a double pendulum and have the values of it be constantly adjustable.</p>

<p> To start this project, I mathematically calculated the trajectory of a double pendulum using my knowledge of dynamics which my professor has bestowed upon me.</p>
Here is an image of a double pendulum.
<img src= "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Double-Pendulum.svg/800px-Double-Pendulum.svg.png" alt = "Pendulums"></img>


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
- $y_1''=\theta_1l_1sin(\theta_1)$
- $x_2''= x_1'+\theta_2'l_2cos(\theta_2)$
- $y_2''=y_1'+\theta_2'l_2sin(\theta_2)$

x1'' = −θ1'2 L1 sin θ1 + θ1'' L1 cos θ1
Next, I used Newton's Second Law 


  
# Acknowledgement
- [Professor Ryan Cooper](https://github.com/cooperrc)
- [Gabriel Koleszar](https://github.com/gabekole)

