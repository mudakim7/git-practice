'''
for i in range(5):
    print('hello jskim')

for i in [1,2,3,4,5]:
    print('hello jskim too')
    print('9 * ' + str(i) + ' = ' + str(9 * i))

i = 0
while i < 5:
    print('hello jskim~~')
    i = i + 1

print(list(range(5)))
'''

dan = 9
i = 1

while i<=9:
    # print('%s*%s=%s' % (dan, i, dan * i))
    print(f'{dan}*{i}={dan*i}')
    i = i + 1