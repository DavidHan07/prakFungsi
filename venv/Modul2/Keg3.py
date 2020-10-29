
a = (2,8,5)

def penjumlahan(inp):
    for i in inp:
        print("Penjumlahan dengan  :", i)
        for y in range(2,5):
            print(i, "+", y,"=",i+y)

def pengurangan(inp):
    for i in inp:
        print("Pengurangan dengan  :", i)
        for y in range(2,5):
            print(i, "-", y,"=",i-y)

def perkalian(inp):
    for i in inp:
        print("Perkalian dengan  :", i)
        for y in range(2,5):
            print(i, "x", y,"=",i*y)

def pembagian(inp):
    for i in inp:
        print("Pembagian dengan  :", i)
        for y in range(2,5):
            print(i, ":", y,"=",i/y)

print("========PENJUMLAHAN========")
penjumlahan(a)
print("========PENGURANGAN========")
pengurangan(a)
print("========PERKALIAN========")
perkalian(a)
print("========PEMBAGIAN========")
pembagian(a)