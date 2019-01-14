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

    field[location[0]+1,location[1]+1] += 3
    field[location[0]+0,location[1]+1] += 3
    field[location[0]+1,location[1]+0] += 3
    field[location[0]+1,location[1]+2] += 3
    field[location[0]+2,location[1]+1] += 3

    print
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


plt.clf()
plt.ion()
plt.figure(figsize=(size[0],size[1]), dpi= 10.0, frameon= False)
plt.pcolor(fieldP)
#plt.colorbar()
figname = "frame_%d.png" % (ii)
plt.savefig(figname)

