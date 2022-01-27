import random

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
	response=input('Response(B,Y,G) : ')
	print(guess, response)
	print("\n\n")
	if(response=='ggggg'):
		print(f'Done. You solved it in {i+1} tries')
		break
	words=change(words, guess, response)