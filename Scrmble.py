def func(word):
	num = int(len(word))
	sword = []
	con = 0
	apnum = 0
	count = 0
	while count < num :
		count += 1	 
		sword.append(word[apnum])
		con += 1
		sword.append(apnum)
		apnum += 1
		con += 1
	
	a = sword.pop(0)
	a = sword.pop(0)
	swordp = ''.join(str(i) for i in sword)	
	print(swordp)
inp = " " + input()
func(inp)
		
