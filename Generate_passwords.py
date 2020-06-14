import random


def strong():
    a = random.randint(20, 40)
    s = ''
    print(a)
    for i in range(1, a):
        aa = random.randint(0, 2)
        aaa = random.randint(1, 100)
        c = random.choice("aertuiopqsdfghjklmcvbn")
        c2 = random.choice("aertuizyxopqsdfghjklmcvbn")
        if aa == 0:
            if aaa > a:
                i = aaa-a
            else:
                i = a-aaa
            s = s+c + c2 + str(i)
        else:
            s += c+c2
    print(s)


def medium():
    a = random.randint(12, 20)
    s = ''
    print(a)
    for i in range(1, a):
        aa = random.randint(0, 2)
        aaa = random.randint(1, 50)
        c = random.choice("aertuiopqsdfghjklmcvbn")
        if aa == 0:
            if aaa > a:
                i = aaa - a
            else:
                i = a - aaa
            s = s + c + str(i)
        else:
            s += c
    print(s)


def weak():
    a = random.randint(6, 10)
    s = ''
    print(a)
    for i in range(1, a):
        aa = random.randint(0, 2)
        aaa = random.randint(1, 20)
        c = random.choice("aertuiopqsdfghjklmcvbn")

        if aa == 0:
            if aaa > a:
                i = aaa - a
            else:
                i = a - aaa
            s = s + c + str(i)
        else:
            s += c
    print(s)


a = input("Strong, Medium or a Weak Password")

if a =="strong":
    strong()
elif a=="medium":
    medium()
elif a=="weak":
    weak()


