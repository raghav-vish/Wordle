'''
Automatic Wordle Solver

Works on the Wordle archive on metzger.media. I might add support for the official Wordle website later.
To use, run the program, switch to the wordle window and let the program run its magic.
Note: There are some bugs. This is a very simple program for which I put the base logic together in like 10 minutes without much thought/

'''

import random
import pyautogui
import time
import PIL.ImageGrab

def change(words, guess, response):
	g=[]
	for i in range(5):
		if(response[i]=='g'):
			g.append([guess[i], i])
	todel=[]
	for word in words:
		for i in range(len(g)):
			if(word[g[i][1]]!=g[i][0]):
				todel.append(word)
	for x in todel:
		if(x in words):
			words.remove(x)

	y=[]
	for i in range(5):
		if(response[i]=='y'):
			y.append([guess[i], i])
	todel=[]
	for word in words:
		for i in range(len(y)):
			if(y[i][0] not in word):
				todel.append(word)
				break
			if(word[y[i][1]]==y[i][0]):
				todel.append(word)
	for x in todel:
		if(x in words):
			words.remove(x)

	b=[]
	for i in range(5):
		if(response[i]=='b' and guess.count(guess[i])==1):
			b.append(guess[i])
			
	todel=[]
	for word in words:
		for i in range(len(b)):
			if(b[i] in word):
				todel.append(word)
				break
	for x in todel:
		if(x in words):
			words.remove(x)
	print(words)
	return words

def check_response(y):
	response=''
	x=790
	for j in range(5):
		r,g,b = PIL.ImageGrab.grab().load()[x,y]
		if(r==0 and g==143 and b==31):
			response+='g'
		elif(r==209 and g==173 and b==71):
			response+='y'
		else:
			response+='b'
		x+=71
	return response

with open('words.txt') as f:
	tempwords = f.readlines()
words=[]
for i in range(len(tempwords)-1):
	tempwords[i]=tempwords[i][:-1].lower()
for word in tempwords:
	if(len(word)==5):
		words.append(word)

for i in range(10000):
	guess=words[random.randint(0, len(words)-1)]
	print(f'Guess : {guess}')
	time.sleep(2)
	pyautogui.typewrite(guess,interval=0.1)
	time.sleep(0.5)
	pyautogui.hotkey('enter')
	time.sleep(2)
	response=check_response(175+(72*i))
	print(guess, response)
	print("\n\n")
	if(response=='ggggg'):
		print(f'Done. You solved it in {i+1} tries')
		break
	words=change(words, guess, response)