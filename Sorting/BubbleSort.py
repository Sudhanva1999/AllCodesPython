def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
print('Enter space separated Elements.')
arr=list(map(int,input().split()))
bubble_sort(arr)
print(arr)
