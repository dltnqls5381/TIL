arr=[2,4,7,9,11,19,23] # 9이하가 low지점
arr.sort()

def binarysearch(target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low +high)//2
        #1.가운데 값이 정답인 경우
        if arr[mid] ==target:
            return mid
        #2.가운데 값이 정답보다 작은경우
        elif arr[mid]< target:
            low = mid +1
        #3.가운데 값이 정답보다 큰 경우
        else:
            high = mid -1
    return "해당 데이터는 없습니다."

print(f'9={binarysearch(9)}')
print(f'4={binarysearch(4)}')
print(f'10 = {binarysearch(10)}')
