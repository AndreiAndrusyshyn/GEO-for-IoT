from pexpect import pxssh
s = pxssh.pxssh()
if not s.login ('<ip>', '<name_to_login>'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    s.sendline('sudo classic')
    s.sendline ('cd p && sudo python script.py')
    s.prompt()         # match the prompt
    print s.before     # print everything before the prompt.
    s.logout()
