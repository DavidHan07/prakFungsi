a = [3,4,8,-2]

def cari(inp):
    out = []
    for y in inp:
        if y > 0 and y % 2 == 0 :
            out.append(y)
    print(out)

filcheck = list(filter(lambda x:  x > 0 and x % 2 == 0 , a))

print(filcheck)
print("================")
cari(a)