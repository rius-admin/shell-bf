#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Editor recode Mr.Rius
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

print "===================================================================== "
print "   "
print "   "
print "    ------------------------ "
print "   "[•] Cyber Sederhana Team [•]"
print "    ------------------------ "
print "   "
print "		"           
print "===================================================================== "
def findAdmin():
	f = open("shell.txt","r");
	link = raw_input("contoh ; target.co  \n bot-robots(scan) : ")
	print "   "
	print "   "
	print "\n\nbot-robots(scan) : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "hasil  => ",req_link

def Credit():
	Space(9); print "  ------------------------"
	Space(9); print "[•] cybersederhanateam.id [•]"
	Space(9); print "  ------------------------"
	Space(9); print " "
  Space(9); print " "

Credit()
findAdmin()
