
List1= ['jurusan', 'praktikum', 'kampus', 'tahun']
List2 = ['informatika', 'fungsional', 'UMM', '2020']

a = [List1[0]+List2[0], List1[1]+List2[1], List1[2]+List2[2], List1[3]+List2[3]]
b = list(map(lambda x : x.lower(),a))
c1 = list(map(lambda x : x.capitalize(),List1))
c2 = list(map(lambda x : x.capitalize(),List2))
c3 = (c1[0]+c2[0], c1[1]+c2[1], c1[2]+c2[2], c1[3]+c2[3])
d = tuple(map(lambda x : x.upper(),a))
e = {List1[0] : List2[0],
     List1[1] : List2[1],
     List1[2] : List2[2],
     List1[3] : List2[3]}


print(a)
print(b)
print(c3)
print(d)
print(e)



