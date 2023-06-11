#!/bin/python3

import sys

import socket

from datetime import datetime

if len(sys.argv) ==2:

	target = socket.gethostbyname(sys.argv[1])

else:

	print("Input error")
print("""    0*-@#      
   *-@#*      ________  __________  ________  ____________  _______       
  *-@#*-      |      |  |        |  |      |        |       |\     |   |\     |   
 *-@#*-*      |      |  |        |  |      |        |       | \    |   | \    |  
*-@#*--*@     |______|  |        |  |______|        |       |  \   |   |  \   |  
*-@#*---#     |         |        |  | \             |       |   \  |   |   \  | 
*-@#*--*@     |         |        |  |  \            |       |    \ |   |    \ |
 *-@#*-       |         |________|  |   \ by@mazer0P|       |_____\|   |     \|
  *-@#*                 
   *-@#     """)
print("-"*50)

print("Scanning target: " +target)

print("Time Started :"+str(datetime.now()))

print("-"*50)

try:

	for port in range(79,82):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port))

		if result ==0:

			#print(f"port {port} is open")
			start = open("openports.txt","w")
			start.write("Open Ports:\n")
			start.close()
			ports = open("openports.txt","a")
			ports.write("\n"+str(port))
			ports.close()
			op = open("openports.txt","r")
			print(op.read())
			 

			s.close()

except KeyboardInterrupt:

	print("Exiting the scanner")

	sys.exit()

except socketgaierror:

	print("hostname cannot be resolved")

	sys.exit()

except socket.error:

	print("Could not connect to host")

	sys.exit()
