def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1 
        else:
            high=mid-1
    return -1 
array=[10,40,50,70]
targ=50
print(binarysearch(array,targ))
