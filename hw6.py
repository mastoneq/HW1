# Question 1a:
#T(infinity)>/ (1-p)T(1)+p(T1)/ infinity = (1-p)T(1) + 0
#Speedup = T(1)/((1-p)T(1))

from __future__ import division
from matplotlib import pyplot as plt
import numpy
import sys
 
# Question 1b:  
def speedup(t,p,n):
	su = t/((1-p)*t + p*t/n)
	return su

for n in range(1,16384):
	su = speedup(395,0.5,n)
	plt.plot(n,su,'ro')
	
plt.ylabel('speedup')
plt.xlabel('number of processors')
plt.xscale('log')
plt.show()	

# Question 1c: 	Use the above function to compare on one graph the speedups 
# possible (for various numbers of processors) for p=0.5,0.67,0.95,0.99.

for p, dottype in zip([0.5,0.67,0.95],['ro','bs','g^']):
	for n in range(1,16384):
		su = speedup(395,p,n)
		plt.plot(n,su,dottype)
	
plt.ylabel('speedup')
plt.xlabel('number of processors')
plt.xscale('log')
plt.show()

#Question 2


import time
from multiprocessing import Array, Pool
from matplotlib import pyplot

# initial conditions
y = multiprocessing.Array('d', 1000, lock=False)
y[480:520] = [1] * 40

# time-step
dt = 0.01


# allows passing of array to pool function via initializer argument
def init_process(y_to_share, new_y_to_share):
	global y, new_y
	y = y_to_share
	new_y = new_y_to_share

# our rule for reaction-diffusion
def advance(dt):
	global y
	n = len(y)
	new_y = list(y)
	for j in xrange(n):
		new_y[j] += dt * (20 * (y[j - 1] - 2 * y[j] + y[(j + 1) % n])
						   - y[j] * (1 - y[j]) * (0.3 - y[j]))
	y = new_y

	

# advance through t (t = i * dt) is at least 100; plot
# every 20

if __name__ == '__main__':

#for numprocesses in list[1,2,4,8,16]

	process_pool = multiprocessing.Pool(processes=4, initializer=init_process, initargs=(y, new_y))

	start = time.time()
	
#	len_interval = int( / numprocesses)
#	intervals = [i*len_interval, (i+1) * len_interval for i in xrange(num_processes)
	
	
	i = 0
	while i * dt <= 100:
		if i * dt % 20 == 0:
			pyplot.plot(y, label='t = %g' % (i * dt))
		advance(dt)
		i += 1
		print i * dt

	process_pool.map(

	stop = time.time()
	pyplot.legend()
	pyplot.show()



