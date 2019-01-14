#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Thu Jan 10 11:39:31 2019

#@author: aarsh



import time
import numpy
import random
from matplotlib import pyplot as plt

size = (100,100)

max_height = 4


initial_height = 0
location = (49,49)

field = numpy.zeros((size[0]+2,size[1]+2))
NField = field.size

for ii in range (size[0]+2):
    for jj in range (size[1]+2):

        field[ii][jj] = random.randint(0,3)
    
NN = 400
t0 = time.time()
    
for ii in range (NN):

    '''field[location[0]+1,location[1]+1] += 3
    field[location[0]+0,location[1]+1] += 3
    field[location[0]+1,location[1]+0] += 3
    field[location[0]+1,location[1]+2] += 3
    field[location[0]+2,location[1]+1] += 3
'''
    #print
while numpy.max(field) >= max_height:
    
    highest = numpy.argmax(field.reshape(1,field.size))
    
    x = int(int(highest) / int(field.shape[0]))
    y = int(int(highest) % int(field.shape[0]))
    
    field[x,y] -= 4
    field[x-1,y] += 1
    field[x+1,y] += 1
    field[x,y-1] += 1
    field[x,y+1] += 1
        
    field[0,:] = 0
    field[:,0] = 0
    field[size[0]+1,:] = 0
    field[:,size[1]+1] = 0
        
      
    
fieldP = numpy.copy(field[1:size[0], 1:size[1]])
#print (fieldP)

fourier = []
fourier.append(numpy.fft.fft2(fieldP))
#print (fourier)
power_spectrum = []
power_spectrum.append(numpy.abs(fourier))
#print (power_spectrum)
power_spectrum = numpy.array(power_spectrum[0][0])
#print (power_spectrum)
power_spectrum = numpy.fft.fftshift(power_spectrum)
power_spectrum = numpy.array(power_spectrum)
print (power_spectrum)
def azimuthal_average(plot):
    x, y = numpy.indices(plot.shape)
    
    center = numpy.array([(x.max()-x.min())/2.0, (y.max()-y.min())/2.0])
    r = numpy.hypot(x - center[0],y - center[1])
    print (r)
    n = numpy.argsort(r.flat)
    sorted_radii = r.flat[n]
    sorted_plot = plot.flat[n]
    
    r_int = sorted_radii.astype(int)
    
    delta_r = r_int[1:] - r_int[:-1]
    changed_r = numpy.where(delta_r)[0]
    nr = changed_r[1:] - changed_r[:-1]
    
    cumulative_sum = numpy.cumsum(sorted_plot, dtype=int)
    total = cumulative_sum[changed_r[1:]] - cumulative_sum[changed_r[:-1]]
    
    average = total / nr
    
    return average

a_average = azimuthal_average(power_spectrum)
a_average = numpy.array(a_average)
#print (a_average)
    
#plt.clf()
#plt.ion()
#plt.figure(figsize=(size[0],size[1]), dpi= 10.0, frameon= False)
#plt.pcolor(fieldP)
#plt.colorbar()
#figname1 = "frame_%d.png" % (ii)
#plt.savefig(figname1)

#plt.clf()
#plt.ion()
#plt.figure(figsize=(size[0],size[1]), dpi= 10.0, frameon= False)
#plt.pcolor(fourier)
#plt.colorbar()
#figname2 = "fourier.png" % (ii)
#plt.savefig(figname2)
'''
plt.clf()
plt.ion()
plt.figure(figsize=(size[0],size[1]), dpi= 20.0, frameon= False)
plt.pcolor(power_spectrum)
plt.colorbar()
figname3 = "power_spectrum.png"
plt.savefig(figname3)
#plt.show()
'''


plt.plot(a_average)