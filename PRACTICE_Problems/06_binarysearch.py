 
def nd(list, n):  
    low = 0  
    high = len(list) - 1  
    mid = 0  
  
    while low <= high:    
        mid = (high + low) // 2  
     
        if list[mid] < n:  
            low = mid + 1  

        elif list[mid] > n:  
            high = mid - 1  
  
        else:  
            return mid  

    return -1  
  
 
list = [1,10,35,40, 45, 50, 54,99,1221]  
n = 45  
    
if nd(list, n) != -1:  
    print("Element is present at index",nd(list, n)) #calling function at same line
else:  
    print("Element is not present in list1")  