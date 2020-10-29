angka = [15,4]


for x in angka:
    if x > 0:
        for y in range(2, x):
            if x % y == 0:
                if x % 2 == 1:
                    print(x, 'adalah bilangan ganjil')
                    break
                print(x, 'adalah bilangan genap')
                break
        else:
            if x == 1:
                print(x, 'adalah bilangan ganjil')
            else :
                print(x, 'adalah bilangan prima')
    else :
        if x % 2 == 0:
            print(x, "adalah bilangan genap")
        else:
            print(x, 'adalah bilangan ganjil')



