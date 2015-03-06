#!/usr/bin/python

import socket, multiprocessing, time, sys

numberofthreads=8
address = sys.argv[1]
lowport = int(sys.argv[2])
highport = int(sys.argv[3])
numberofports = highport - lowport + 1
print "numberofports = %d"%numberofports
portset =  range(lowport, highport+1)

#divide ports up in to even groups based on the number of threads

def portwork(low, high):
	for x in range(low, high+1):
		tcp = socket.socket()
		tcp.settimeout(.5)
		if (tcp.connect_ex((address,x)) == 0):
			print "port %d is open"%x
		tcp.close()
if __name__ == '__main__':
	groupsize = numberofports / numberofthreads
	print "groupsize = %d"%groupsize
	for x in range(numberofthreads):
		low = groupsize * x
		high = low + groupsize
	
		p = multiprocessing.Process(target=portwork, args=(low,high))
		lock = multiprocessing.Lock()
		p.start()

#clean up remainder
	if numberofports - groupsize * numberofthreads > 0:
		remainder = numberofports - groupsize * numberofthreads
		for x in range(groupsize * numberofthreads, numberofports):
			print "x = %d"%x
	
