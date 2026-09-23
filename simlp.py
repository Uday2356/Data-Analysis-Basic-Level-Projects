def rotate( arr , k):
    if  len(arr)==1:
        return arr
    
    nums1 = arr[k:]
    nums2 = arr[:k]

    return nums1+nums2


arr = [1,2,3,4,5,6,7]
k = 3

print(rotate(arr,k))




    