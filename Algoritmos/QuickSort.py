
#	θ(n log(n))
def partition(list,low,high):
    i = (low-1)
    pivot = list[high]

    for j in range(low,high):
        if(list[j]<=pivot):
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1] 
    return (i+1) 



def quickSort(list, low, high): 
    if len(list) == 1: 
        return list 
    if low < high: 
  
        pi = partition(list, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(list, low, pi-1) 
        quickSort(list, pi+1, high) 

list = [8,11,11,30,45,82,191,212,220,283,325,326,345,363,394,425]

n = len(list)

quickSort(list,0,n-1)

print(list)