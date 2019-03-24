from pexpect import pxssh
import numpy as np
import time

s = pxssh.pxssh()
y = (list((n) for n in range(310, 0, -1))) + (list((n+100) for n in range(500)))
print(y)
while True:
	if not s.login ('<ip>', '<name>'):
		print ("SSH session failed on login.")
		print (str(s))
	else:
		print ("SSH session login successful")
		s.sendline('sudo classic')
		s.sendline ('cd p')
	for i in y:
		time.sleep(1)		
		s.sendline('sudo python write.py '+str(i))

	s.prompt()         
	print (s.before)	
	s.logout()

