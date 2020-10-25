#Arunava Nag; CS 622 Project 2
#!/usr/bin/env python
import numpy as np
import random
import math as m

#function to find gradient descent 

def gradient_descent(f, x_init, eta):
    precision = 0.00001                 #value the gradient will get close to
    max_iter = 1000                     #limiting max epochs
    count = 0                           #counter for the epochs to reach precision
    step_size = [eta,eta]               #declaring a initial stepsize
    while any(a > precision for a in step_size) and count < max_iter:           
        x = x_init                      #storing old x
        x_init = x_init - eta*f(x)      #gradient descent
        step_size = abs(x_init - x)     
        count+=1    
    return x