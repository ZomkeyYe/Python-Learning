if __name__ == '__main__':
    while True:
        try:   
            lis = list(map(int,input().split()))
            arr = input().split()
            x = lis[1]
            print(" ".join(arr[-x:]+arr[:-x]))
        except:
            break
