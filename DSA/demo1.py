num = 10
arr =[12,34,10,55]

def search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False

def average(arr):
    return sum(arr) / len(arr)

print(f"The number {num} is present in the array -",search(arr,num))

print("Average of this array is", average(arr))