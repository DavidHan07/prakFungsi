a = [3,4,8,-2]

def primebiasa(x):
    for num in x:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "is not a prime number")


def primecheck(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num, "is not a prime number")
        
check = list(map(primecheck, a));
print("==========================")
primebiasa(a)

''''
def cari(inp):
    out = []
    for y in inp:
        if y > 0 and y % 2 == 0 :
            out.append(y)
    print(out)


def cari2(y):
    if y > 0 and y % 2 == 0 :
        return y



check = list(map(cari2, a));
print(check)
cari(a)
'''