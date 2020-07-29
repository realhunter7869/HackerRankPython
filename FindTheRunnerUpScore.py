# !st Approach


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(set(arr))
    lst.sort(reverse = True)
    largest = lst[0]
    for number in lst:
        if largest != number:
            print(number)
            break

        
# 2nd Approach


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = max(arr)
    while largest == max(arr):
        arr.remove(max(arr))
    print(max(arr))
    
    
