
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    runner_up_score=0
    for  num in arr:
        if (num<arr[0]):
            runner_up_score=num
            break
    print(runner_up_score)