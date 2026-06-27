'''
bts = []
bts.append("V")
print(bts)
bts = bts + ['RM']

print(bts)

print(list(range(5)))
print([0,1,2] * 3)

print([x ** 2 for x in [1, 2,3] if x % 2 == 0])

a, b = 1, 2
(a, b) = (b, a)
print(a,b)

p = {'a' : 1, 'b' : 2}
print(p.keys())
'''
s = 'welcome, to , python and bla,bla'
print([x.strip() for x in s.split(',')])

print(list('Welcom to python'))

print('-'.join('010.1111.2222'.split('.')))
print(max(s))