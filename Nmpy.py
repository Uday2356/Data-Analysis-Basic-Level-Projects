import numpy as np 
arr = np.array([20,24,34,45,56,67,56,56])
brr = np.array([10,20,30,60,50,60,60,60])


# 1 = np.zeros() / np.ones()

t = np.zeros(5) #it generate the array of 5 zeroes 
r = np.ones((2,3))#it generate the 2D array of 2 rows and 3 coloumns 
# print(t,'\n',r)


# 2 = np.arange(start : stop : steps) the steps argument is not neccsary to pass 

t = np.arange(0,18,2)
y = np.arange(1,18)
# print(t, '\n' , y)

# 3 = np.linspace(start : stop : points)  Create N evenly spaced points between start and stop.
# if point argument not passed it will print all possible number between start and stop 

t = np.linspace(0,1)
# print(t)

# 4 = np.eye(row , columns) it create the Identity matrix 1s on the diagonal and 0s elsewhere

t = np.eye(3)
# print(t)

# 5 = np.random.rand() 

t = np.random.rand(3) # this generate random numbers of given size you can pass as row , column or only single argument
# print(t)

# 6 = np.random.randn # this genrate the number whose mean is Zero 
t = np.random.randn(3,3)
print(t.mean())

# 7 = np.random.randint(start , stop , points) # this generate the list of the random numbers   

t = np.random.randint(1,10,5) 
# print(t)
  
# 8 = np.vstack([arr1 , arr2 ]) it stack the arr as rows 
t = np.vstack([arr , brr]) # this dimension get change here from 2 array of 1d it become 1 array of 2d
# print(t) 

# The size of the array must be same 

# 9 = np.hstack([a,b]) It just add the next array at the last 

t = np.hstack([arr,brr])
# print(t) #i

# 10 .shape / .size / .ndim They tell the dimension of the array

t = arr.shape
y = arr.size
u = arr.ndim
# print(u,y)

# arr = np.zeros((2, 3, 4))
# print(arr)

# print(arr.shape)   # (2, 3, 4)
# print(arr.ndim)    # 3

# 11 isnan() / np.isinf()  Detect missing (NaN) or infinite values in data.

t = np.isnan(arr)
# print(t)

t = np.isinf(arr) # for nan value it shows the True 
# print(t)

# 12 np.unique(arr) it only prints the Unique value of the array 
# print(arr)
t= np.unique(arr) 
y = np.unique(arr , return_counts=True) # return the l=lsit in which the frequncy of each element in arr is shown
# print(t,y)

# 13 = np.count_nonzero(condition) # it works to count of basis of condition
t = np.count_nonzero(arr<60)
# print(t)

# 14 np.nan*varients = Safe versions of functions that ignore NaN (missing) values.

# varient = [mean , median , max , min , std , var] 
# they ignore the nabn value and perform operations 

# 15 = np.cumsum() / np.cumprod() ; Running total or running product across the array.

t = np.cumsum(arr)
# print(t)







