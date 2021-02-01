
#O(Log n)
def binarySearch(list, value):
    low = 0
    high = len(list)
    mid = 0
    while (low<=high):
        mid = (low+high)//2;
        if(list[mid]==value):
            return mid
        elif(list[mid]<value):
            low = mid+1
        else:
            high = mid - 1
        
    return -1


list = [8,11,11,30,45,82,191,212,220,283,325,326,345,363,394,425]

list.sort()

print(list)
print(binarySearch(list,40))