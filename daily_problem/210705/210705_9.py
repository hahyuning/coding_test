from bisect import bisect_left

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        b = []

        for i in range(n):
            if not b:
                b.append(a[i])
                continue

            j = bisect_left(b, a[i])
            # a[i]가 b에 있는 수들보다 큰 경우
            if j >= len(b):
                b.append(a[i])
            # 전에 삽입한 수보다 a[i]가 작은 경우
            # 바꾸기 전에 이미 최대 길이가 나오더라도 개수는 그대로 보존되므로 ok
            # 바꾸고 나서 더 긴 수열이 나오는 경우에는 계속 추가하면 된다.
            else:
                b[j] = a[i]

        print(len(b))
    except:
        break