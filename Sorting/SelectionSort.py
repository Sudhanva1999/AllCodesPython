def selection_sort(arr):
    for i in range(len(arr)):
        m=999
        for j in range(i,len(arr)):
            if arr[j]<m:
                m=arr[j]
                pos=j
        arr[i],arr[pos]=m,arr[i]
        print(arr[i],arr[pos])

        
print('Enter space separated Elements.')
arr=list(map(int,input().split()))
selection_sort(arr)
print(arr)
