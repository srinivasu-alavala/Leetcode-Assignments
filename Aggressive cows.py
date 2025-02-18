def max_min_distance(n, c, stalls):
    stalls.sort()  
    low, high = 0, stalls[-1]  
    best = 0

    while low <= high:
        mid = (low + high + 1) // 2  
        count = 1  
        left = 0

       
        for i in range(1, n):
            if stalls[i] - stalls[left] >= mid:
                count += 1
                left = i
                if count == c:
                    break

        
        if count >= c:
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best



t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    stalls = [int(input()) for _ in range(n)]
    print(max_min_distance(n, c, stalls))
