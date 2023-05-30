import numpy as np

arr=np.random.randint(10,99,size=100)

mini=10
maxi=99

arr1=[]
for i in range(100):
    arr1.append((arr[i]-mini)/(maxi-mini))

print(arr1)
