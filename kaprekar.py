def largest_digit(num):
    numlist = []
    numfill = num.zfill(4)
    for i in numfill:
        numlist.append(i)
        numlist.sort(reverse=True)
    numlista = ''.join(numlist)
    return numlist[0] , numlista
def bigtosmall(a):
    a = str(a)
    alist = []
    afill = a.zfill(4)
    for i in afill:
        alist.append(i)
        alist.sort(reverse=True)
    alista = ''.join(alist)
    return alista
def smalltobig(b):
    b = str(b)
    blist = []
    bfill = b.zfill(4)
    for i in bfill:
        blist.append(i)
        blist.sort()
    blista = ''.join(blist)
    return blista
def kaprekar_num(numkap):
    count = 0
    while int(numkap) != 6174:
       numkap = int(bigtosmall(numkap)) - int(smalltobig(numkap))
       count += 1
    return count
inp = input()
print(largest_digit(inp))
print(kaprekar_num(inp))