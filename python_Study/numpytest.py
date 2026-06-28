import numpy as np

y = [[[1,2],[3,3]],[[4,5],[6,6]],[[7,8],[9,9]]]
#print(y)

np_array = np.array(y)
#print(np_array)


#print(np.random.rand(5))

np.random.seed(100)
print(np.random.rand(5))
print(np.random.rand(5,3))
print(np.random.rand(5))

np.random.seed(100)
print(np.random.rand(5))
print(np.random.rand(5))
print(np.random.rand(5,3))
print(np.random.rand(5))

print(list(range(5)))