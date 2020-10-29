
a = (2,8,5)

def penjumlahan(inp):
    for i in inp:
        print("Penjumlahan dengan  :", i)
        for y in range(2,6):
            print(i, "+", y,"=",i+y)


penjumlahan(a)