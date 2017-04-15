import random
while True:

    def random_secenek(count):
        countl = 0
        
        count = int(count)
        while countl < count:
            countl += 1
            a = random.randint(1, 5)
            if a == 1:
                print("A")
            elif a == 2:
                print("B")
            elif a == 3:
                print("C")
            elif a == 4:
                print("D")
            elif a == 5:
                print("E")
    random_secenek(input("Soru sayısı:"))

