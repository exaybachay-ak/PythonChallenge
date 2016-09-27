# Challenge 5 URL
# http://www.pythonchallenge.com/pc/def/linkedlist.php

#hint0 = <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
#end. 400 times is more than enough. -->

#hint1 = "linkedlist.php?nothing=12345"
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827

#hint2 = and the next nothing is 44827
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827
# and the next nothing is 45439

#hint3 = and the next nothing is 45439
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439
# Your hands are getting tired and the next nothing is 94485



#answer is here: https://docs.python.org/2/library/urllib.html

#strategy:
# use urllib to open the nothing URLs and extract number after "next nothing is" 
# iterate through 400 nothing URLs this way

#initialize first nothing

#def iterateNothings():
#	x = 1
#
#	while < 400:
#		filehandle = urllib.urlopen(http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345)
#
#		x += 1
#		print 

import urllib

#filehandle = urllib.urlopen(http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345)
#print filehandle

def openPages():
	i = 12345
	while i < 200000:
		#initialize urllib opener
		opener = urllib.FancyURLopener({})
		t = str(i)
		url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + t + ""

		#define the URL to look at
		f = opener.open(url)
		#f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + i + "")
	
		f.read()
		#if f.read() returns any information, print the URL
		if f.read():
			print f.read()
		i += 1

		#print t
openPages()
