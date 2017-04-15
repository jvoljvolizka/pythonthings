def morse_trans(word):
	code_dic = { "a" : "dalyarak " ,
				 "b" : "yarakdaldaldal " ,
				 "c" : "yarakdalyarak " ,
				 "d" : "yarakdaldal " ,
				 "e" : "dal " ,
				 "f" : "daldalyarakdal " ,
				 "g" : "yarakyarakdal " ,
				 "h" : "daldaldaldal " ,
				 "i" : "daldal " ,
				 "j" : "dalyarakyarakyarak " ,
				 "k" : "yarakdalyarak " ,
				 "l" : "dalyarakdaldal " ,
				 "m" : "yarakyarak " ,
				 "n" : "yarakdal " ,
				 "o" : "yarakyarakyarak " ,
				 "p" : "dalyarakyarakdal " ,
				 "q" : "yarakyarakdalyarak " ,
				 "r" : "dalyarakdal " ,
				 "s" : "daldaldal " ,
				 "t" : "yarak " ,
				 "u" : "daldalyarak " ,
				 "v" : "daldaldalyarak " ,
				 "w" : "dalyarakyarak " ,
				 "y" : "yarakdalyarakyarak " ,
				 "z" : "yarakyarakdaldal " ,
				 "1" : "dalyarakyarakyarakyarak " ,
				 "2" : "daldalyarakyarakyarak " ,
				 "3" : "daldaldalyarakyarak " ,
				 "4" : "daldaldaldalyarak " ,
				 "5" : "daldaldaldaldal " ,
				 "6" : "yarakdaldaldaldal " ,
				 "7" : "yarakyarakdaldaldal " ,
				 "8" : "yarakyarakyarakdaldal " ,
				 "9" : "yarakyarakyarakyarakdal " ,
				 "0" : "yarakyarakyarakyarakyarak " ,
				 " " : "/"}

	lowerword = word.lower()
	morse_list = []
	for i in lowerword:
		morse_list.append(code_dic[i])
	print(''.join(morse_list))

morse_trans(input())